from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
import requests
from datetime import datetime
from django.conf import settings
from .utils import get_access_token, generate_password


@method_decorator(csrf_exempt, name='dispatch') 
class InitiateSTKPush(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            amount = data.get('amount')
            phone = data.get('phone') 

            if not amount or not phone:
                return JsonResponse({'error': 'Amount and Phone are required'}, status=400)

            access_token = get_access_token()
            if not access_token:
                return JsonResponse({'error': 'Failed to authenticate with M-Pesa'}, status=503)

            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            password = generate_password(timestamp)
            
            callback_url = "https://kyler-unwrung-umbrageously.ngrok-free.dev/api/payments/callback/"



            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

            payload = {
                "BusinessShortCode": settings.MPESA_SHORTCODE,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": phone, 
                "PartyB": settings.MPESA_SHORTCODE, 
                "PhoneNumber": phone,
                "CallBackURL": callback_url,
                "AccountReference": "Blyator Technologies", 
                "TransactionDesc": "Payment for Services"
            }

            response = requests.post(
                f"{settings.MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest",
                json=payload,
                headers=headers
            )
            
            return JsonResponse(response.json())

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


# 2. CALLBACK HANDLER 
@method_decorator(csrf_exempt, name='dispatch')
class MpesaCallback(View):
    def post(self, request):
        # Safaricom sends JSON data here
        try:
            body = request.body.decode('utf-8')
            data = json.loads(body)
            
            # Use 'stkCallback' key to access data
            stk_callback = data.get('Body', {}).get('stkCallback', {})
            result_code = stk_callback.get('ResultCode')

            if result_code == 0:
                # SUCCESS
                metadata = stk_callback.get('CallbackMetadata', {}).get('Item', [])
                
                # Extract details (Receipt, Amount, Phone)
                mpesa_receipt = next((item['Value'] for item in metadata if item['Name'] == 'MpesaReceiptNumber'), None)
                amount = next((item['Value'] for item in metadata if item['Name'] == 'Amount'), None)
                phone = next((item['Value'] for item in metadata if item['Name'] == 'PhoneNumber'), None)

                print(f"Payment Success: {mpesa_receipt} for {amount} from {phone}")
                
                
            else:
                # FAILED 
                print(f"Payment Failed. Code: {result_code}")

            # Always return a success response to Safaricom so they stop retrying
            return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})

        except Exception as e:
            print(f"Error processing callback: {e}")
            return JsonResponse({"error": "failed"}, status=500)