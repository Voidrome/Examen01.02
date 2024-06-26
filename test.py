from datetime import datetime
from collections import defaultdict

def get_sorted_dates(purchase_dates):
    month_counts = defaultdict(int)
    
    for date_time_str in purchase_dates:
        dt = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        month_key = dt.strftime('%Y-%m-01 00:00')
        month_counts[month_key] += 1
    
    sorted_months = sorted(month_counts.keys(), key=lambda x: (month_counts[x], x), reverse=True)
    
    return sorted_months

if __name__ == "__main__":
    purchase_dates = [
        '2019-12-12 14:43',
        '2019-12-01 15:05',
        '2019-11-04 09:01',
        '2019-11-30 18:30',
        '2019-11-02 10:15',
        '2019-10-05 08:00',
        '2019-10-15 20:30',
        '2019-10-01 12:00'
    ]
    
    sorted_dates = get_sorted_dates(purchase_dates)
    
    for date in sorted_dates:
        print(date)