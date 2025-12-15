# M-Pesa Payment Integration

This is a full-stack application showing how to integrate Safaricom's Lipa na M-Pesa STK Push functionality using a Django backend and a React frontend.

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
- **Vite**: Frontend build tool.

### Backend
- **Django 5**
- **Django REST Framework**


## Prerequisites

- Docker
- Docker Compose
- Safaricom Developer Account 

## Getting Started

1.  **Clone the Repository**:
    ```bash
    git clone git@github.com:blyator/M-Pesa-Payment-Integration.git
    cd M-Pesa-Payment-Integration
    ```

2.  **Configure Environment Variables**:
 

3.  **Build and Run with Docker Compose**:
    From the project root directory, execute:
    ```bash
    docker compose up --build -d
    ```

4.  **Access the Application**:
    -    Open your browser to `http://localhost` 


## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/stkpush/` | Initiates an STK Push request. Requires `amount` and `phone` in JSON body. |
| `POST` | `/api/payments/callback/` | Receives payment status updates from Safaricom. |
| `GET` | `/check-status/<checkout_request_id>/` | Checks the status of a specific transaction. |

## Usage

1.  Run Docker Compose services.
2.  Open the application in your browser.
3.  Enter the amount and the M-Pesa phone number (format: `2547...`).
4.  Click "Pay".
5.  Respond to the STK Push prompt on your mobile device 
6.  The application will update the transaction status.

## License

[MIT](LICENSE)
