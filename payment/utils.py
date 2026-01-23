import uuid

def initiate_sslcommerz_payment(payment):
    # generate unique transaction id
    payment.transaction_id = str(uuid.uuid4())
    payment.save()

    # Here you would prepare SSLCommerz payload and return payment URL
    return f"https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?tran_id={payment.transaction_id}"


import uuid

def initiate_sslcommerz_payment(payment):
    payment.transaction_id = str(uuid.uuid4())
    payment.save()

    callback_url = "https://yourdomain.com/api/payments/callback/"

    payload = {
        "tran_id": payment.transaction_id,
        "total_amount": payment.paid_amount,
        "success_url": callback_url,
        "fail_url": callback_url,
        "cancel_url": callback_url,
        "ipn_url": callback_url,
    }
    return "SSLCommerz payment page URL"
