import grpc
from concurrent import futures
import time

# import the generated classes
import metodosgrpc_pb2
import metodosgrpc_pb2_grpc

# import the original calculator.py
import metodosgrpc

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class MetodosDSIDServicer(metodosgrpc_pb2_grpc.MetodosDSIDServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def RetornaVoid(self, request, context):
        response = metodosgrpc_pb2.Empty
        response.value = ""
        return
    def RetornaTeste(self, request, context):
        response = metodosgrpc_pb2.Empty
        response.value = ""
        return
    def Retornalong8param(self, request, context):
        response = metodosgrpc_pb2.oitoLong
        response.value = metodosgrpc.long_8_param(request.a,request.b,request.c,request.d,request.e,request.f,request.g,request.h)
        return
    def retorna1long(self, request, context):
        response = metodosgrpc_pb2.umLong
        response.value = metodosgrpc.long_1_param(request.a)
        return
    def retorna1String(self, request, context):
        response = metodosgrpc_pb2.umLong
        response.value = metodosgrpc.uma_string(request.a)
        return
    def retorna8string(self, request, context):
        response = metodosgrpc_pb2.umLong
        response.value = metodosgrpc.oito_string(request.a,request.b,request.c,request.d,request.e,request.f,request.g,request.h)
        return
    def retorna16string(self, request, context):
        response = metodosgrpc_pb2.umLong
        response.value =  response.value = metodosgrpc.dezeseis_string(request.a,request.b,request.c,request.d,request.e,request.f,request.g,request.h,request.i,request.j,request.k,request.l,request.m,request.n,request.o,request.p)
        return
    def retornaNo(self, request, context):
        response = metodosgrpc_pb2.complexo
        response.value = metodosgrpc.retornaNo(request.a)
        return
    def Vetor(self, request, context):
        response = metodosgrpc_pb2.vetor
        response.value = metodosgrpc.vetor(request.a)
        return
# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
metodosgrpc_pb2_grpc.add_MetodosDSIDServicer_to_server(
        MetodosDSIDServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 8000.')
server.add_insecure_port('[::]:8000')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)