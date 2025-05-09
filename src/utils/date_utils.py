from datetime import datetime


class DateUtils:
    @staticmethod
    def iso_datetime_to_gsheets_serial(iso_datetime: str) -> int:
        if not iso_datetime or iso_datetime.strip() == '':
            return None
        
        try:
            dt_obj = datetime.strptime(iso_datetime, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            try:
                dt_obj = datetime.strptime(iso_datetime.split()[0], '%Y-%m-%d')
            except ValueError:
                try:
                    dt_obj = datetime.strptime(iso_datetime, '%d/%m/%Y')
                except ValueError:
                    try:
                        dt_obj = datetime.strptime(iso_datetime, '%d/%m/%Y %H:%M')
                    except ValueError:
                        return None

        base_date = datetime(1899, 12, 30)
        delta = dt_obj.date() - base_date.date()
        return delta.days
