largernumber=int(input('Enter the larger number-'))
smallernumber=int(input('Enter the smaller number-'))
while(smallernumber):
    numberstore=smallernumber
    numberstore=largernumber%smallernumber
    largernumber=numberstore
LCM=(largernumber*smallernumber)/numberstore
print(LCM)