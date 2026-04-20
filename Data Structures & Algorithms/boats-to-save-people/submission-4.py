class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        sorted_people = sorted(people)
        l,r = 0 , len(people) - 1
        num_boats = 0
        print(sorted_people)
        while l <= r:
            weight = sorted_people[l] + sorted_people[r]

            if weight <= limit:
                l +=1
            r -=1
            num_boats +=1




        return num_boats

        