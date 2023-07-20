class Solution:
    def findMissingNumbers(self, numbers):
            #type numbers: list of float
            #return type: list of int
            
            #TODO: Write code below to return an int list with the solution to the prompt.
            #numbers.sort()
            arr =[]
            uniqueNumbers=[]
            hv= numbers[len(numbers)-1]
            output=[]
            import math
            if len(numbers==0):
                 return "Invalid input"
            else:
                 minimum= math.ceil(min(numbers))
                 maximum= math.ceil(max(numbers))
                 for i in range(minimum, maximum):
                     
                    ctr=0
                    for num in numbers:
                        if num%1 !=0:
                            num=math.ceil(num)
                        if i==num:
                            ctr+=1
                    if ctr==0:
                        output.append(i)
            if output==[]:
                return "None missing"
            return output


            for i in numbers:
                 #round
                numbers[i]= int(numbers[i])

            for i in range(len(numbers)):
                if i not in uniqueNumbers:
                     arr.append(numbers[i])
                     

                    





            for i in range(1, len(numbers)):
                if(numbers[i]!= numbers[i-1] or numbers[i]!= numbers[i-1]+1):
                     arr.append(numbers[i])
                     arr[i]= float(numbers[i])
            return arr

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = float(array[x])

    tc1 = Solution()
    ans = tc1.findMissingNumbers(array)
    print(ans)

if __name__ == "__main__":
    main()
    
#listOfNumbers = [0, 3, 3, 3, 4, 7, 3]  # STEP 1: get the in input
#print(findMissingNumbers(listOfNumbers)) # Step 2: Call a function to handle the input