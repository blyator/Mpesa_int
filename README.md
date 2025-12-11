# M-Pesa Payment Integration

This is a full-stack application sowing how to integrate Safaricom's Lipa na M-Pesa STK Push  functionality using a Django backend and a React frontend.

## Features

- **STK Push Initiation**: Users can enter a phone number and amount to trigger an M-Pesa payment prompt on their device.
- **Real-time Status Updates**: The frontend can check the status of the transaction.
- **Callback Handling**: The backend processes M-Pesa callbacks to verify successful or failed transactions.
- **Transaction Logging**: Stores transaction details (Receipt number, Amount, Status) in a database.

## Technologies Used

### Frontend
- **React**: UI Library.
- **TypeScript**: Static typing.
- **Tailwind CSS**

### Backend
- **Django 5**
- **Django REST Framework**


## Prerequisites

- Node.js (v18 or higher)
- Python (v3.10 or higher)
- PostgreSQL (or any other Django-supported database)
- Safaricom Developer Account (for API credentials)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd M-Pesa-Payment-Integration
```

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create and activate a virtual environment:

```bash
# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

**Environment Configuration**:

Create a `.env` file in the `backend/` directory with the following variables:

```env

DATABASE_URL=your db 

# M-Pesa Credentials
MPESA_CONSUMER_KEY=your_consumer_key
MPESA_CONSUMER_SECRET=your_consumer_secret
MPESA_PASSKEY=your_passkey
MPESA_SHORTCODE=174379
MPESA_BASE_URL=https://sandbox.safaricom.co.ke
MPESA_CALLBACK_URL=https://your-domain.com/api/payments/callback/
```

> **Note**: For local development, use a tunneling service like `ngrok` to expose your localhost to the internet for the `MPESA_CALLBACK_URL`.

Run migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

The backend runs on `http://localhost:8000` by default.

### 3. Frontend Setup

Navigate to the project root (if you are in `backend/`, go back one level):

```bash
cd ..
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend runs on `http://localhost:5173` by default.

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/stkpush/` | Initiates an STK Push request. Requires `amount` and `phone` in JSON body. |
| `POST` | `/api/payments/callback/` | Receives payment status updates from Safaricom. |
| `GET` | `/check-status/<checkout_request_id>/` | Checks the status of a specific transaction. |

## Usage

1.  Open the frontend application in your browser (`http://localhost:5173`).
2.  Enter the amount and the M-Pesa phone number (format: `2547...`).
3.  Click "Pay".
4.  You should receive an STK Push prompt on your mobile device.
5.  Enter your PIN to complete the transaction.
6.  The application handles the callback and updates the transaction status in the database.

## License

[MIT](LICENSE)
