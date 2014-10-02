from datetime import datetime, time

from market.models import NonTradingDay

def market_status(request):
    market_status = 'OPEN'
    market_status_class = 'btn-success'
    market_open = time(9, 30)
    market_close = time(15, 30)
    market_recess_start = time(12, 0)
    market_recess_end = time(13, 30)
    dt = datetime.now()
    if dt.isoweekday() >= 1 and dt.isoweekday() <= 5 and not NonTradingDay.objects.filter(non_trading_date=dt.date()).exists():
        if dt.time() >= market_open and dt.time() < market_close:
            if dt.time() >= market_recess_start and dt.time() < market_recess_end:
                market_status = 'RECESS'
                market_status_class = 'btn-warning'
        else:
            market_status = 'CLOSE'
            market_status_class = 'btn-danger'
    else:
        market_status = 'CLOSE' 
        market_status_class = 'btn-danger'
    return {'market_status': market_status, 'market_status_class': market_status_class}
