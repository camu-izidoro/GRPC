import grpc
import time
from datetime import datetime

# import the generated classes
import voidgrpc_pb2
import voidgrpc_pb2_grpc

ini = time.time()
# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = voidgrpc_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = voidgrpc_pb2.Name()
print("number = ", number)

# make the call
try:
    response = stub.SquareRoot(number)
except(Exception,RuntimeError, TypeError, NameError): 
    pass

fim = time.time()
print("Tempo = ", fim-ini)
# et voilà
print('fim')