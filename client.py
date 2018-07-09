import grpc
import time
from datetime import datetime

# import the generated classes
import metodosgrpc_pb2
import metodosgrpc_pb2_grpc

ini = time.time()
# open a gRPC channel
channel = grpc.insecure_channel('192.168.0.17:7070')

# create a stub (client)
stub = metodosgrpc_pb2_grpc.MetodosDSIDStub(channel)

# create a valid request message
umlong = metodosgrpc_pb2.UmLong(param1=1) #Aqui define o valor de Number

# make the call

response = stub.MetodoUmParametroLong(umlong)


print("resposta", response)
fim = time.time()
print("Tempo = ", fim-ini)
# et voilà
print('fim')