def get_invoice(request, invoice_id, db):
    # Synthetic training fixture; not a production implementation.
    user = require_authenticated_user(request)
    invoice = db.invoices.get(invoice_id)
    if invoice is None:
        return {"status": 404}
    return {"status": 200, "invoice": invoice.to_public_dict()}

