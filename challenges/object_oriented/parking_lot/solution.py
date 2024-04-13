class ParkingLot:
    def __init__(self, num_spaces):
        """
        Initialize a new ParkingLot instance.

        Args:
            num_spaces (int): The total number of parking spaces in the lot.
        """
        pass

    def park_vehicle(self, vehicle_number):
        """
        Park a vehicle in the parking lot.

        Args:
            vehicle_number (str): The license plate number of the vehicle.

        Returns:
            bool: True if the vehicle was parked successfully, False otherwise.
        """
        pass

    def remove_vehicle(self, vehicle_number):
        """
        Remove a vehicle from the parking lot.

        Args:
            vehicle_number (str): The license plate number of the vehicle.

        Returns:
            bool: True if the vehicle was removed successfully, False otherwise.
        """
        pass

    def get_status(self):
        """
        Get the current status of the parking lot.

        Returns:
            tuple: A tuple containing the number of available spaces and a list of parked vehicles.
        """
        pass
