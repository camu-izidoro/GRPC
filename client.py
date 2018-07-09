import grpc
import time
from datetime import datetime

# import the generated classes
import metodosgrpc_pb2
import metodosgrpc_pb2_grpc

ini = time.time()
# open a gRPC channel
channel = grpc.insecure_channel('192.168.0.17:8000')

# create a stub (client)
stub = metodosgrpc_pb2_grpc.MetodosDSIDStub(channel)

# create a valid request message
number = metodosgrpc_pb2.Empty()
print("number = ", number)

# make the call
try:
    response = stub.MetodoVoid(number)
except(Exception,RuntimeError, TypeError, NameError): 
    pass

fim = time.time()
print("Tempo = ", fim-ini)
# et voilà

teste1 = metodosgrpc_pb2.umString()
print("number = ", teste1)

# make the call
try:
    response = stub.MetodoUmParametroString(teste1)
except(Exception,RuntimeError, TypeError, NameError): 
    pass

fim = time.time()
print("Tempo = ", fim-ini)
# et voilà



print('fim')