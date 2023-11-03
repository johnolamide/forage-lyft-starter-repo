from battery import Battery


class SpindlerBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if (last_service_date + 3) > current_date:
            return True
        return False
