import pandas
import numpy

def process_file(filename):
    fl=pandas.read_csv(filename,delim_whitespace=True)
    boughtarray=numpy.asarray(fl['Bought'])
    costarray=numpy.asarray(fl['Cost'])
    consumedarray=numpy.asarray(fl['Consumed'])
    return boughtarray, costarray, consumedarray

# Parantez icine dosya adi gelecek
bought , cost , consumed =  process_file("dt1.txt")

tot=bought*cost

# total cost for buying everything
total_cost=tot.sum()
total_order=bought.sum()

print("Total amount paid: "+ str(total_cost))
print("Total amount ordered: "+ str(total_order))


#monthlycost = numpy.zeros(14)

leftover=0
for i in range(14):

    monthlycost=(cost[i]*(bought[i]-consumed[i]+leftover))

    # Leftover coffee
    leftover = leftover + bought[i] - consumed[i]

print("total cost if not constant: "+ str(monthlycost))


# if order is constant,
bought=numpy.ceil(numpy.average(consumed))

leftover=0
for i in range(14):

    monthlycost=(cost[i]*(bought-consumed[i]+leftover))

    # Leftover coffee
    leftover = leftover + bought - consumed[i]

print("total cost if order is constant: "+str(monthlycost))
