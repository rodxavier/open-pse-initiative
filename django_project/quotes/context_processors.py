from quotes.models import Quote

def latest_quote_date(request):
    latest_quote_date = Quote.objects.latest('quote_date').quote_date
    return {'latest_quote_date': latest_quote_date}
