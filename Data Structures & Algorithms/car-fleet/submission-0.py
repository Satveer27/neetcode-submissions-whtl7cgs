class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for car in range(len(position)):
            cars.append((position[car], speed[car]))
        
        current_cars = []
        sorted_cars = sorted(cars, key=lambda car_set: car_set[0])

        for i in range(len(sorted_cars)-1, -1, -1):
            curr_distance = (target-sorted_cars[i][0])/sorted_cars[i][1]
            if len(current_cars) != 0:
                check_top = current_cars[-1]
                if check_top < curr_distance:
                    current_cars.append(curr_distance)
            else:
                current_cars.append(curr_distance)
        
        return len(current_cars)
