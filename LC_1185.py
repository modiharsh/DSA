# https://leetcode.com/problems/day-of-the-week/description/

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        res=year-1971
        res=res+(year-1968-1)//4
        dic={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        if((year%400==0)or(year%100!=0)and(year%4==0)):
            dic[2]=29
        ans=0
        for k,v in dic.items():
            if k<month:
                ans=ans+v
        ans=ans+day
        print(ans)
        days = ['Thursday', 'Friday','Saturday','Sunday','Monday','Tuesday', 'Wednesday']
        ans=(res+ans)%7
        print(ans)
        return days[ans]

# Example 1:

# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
# Example 2:

# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
# Example 3:

# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
