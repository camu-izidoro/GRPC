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
    def MetodoVoid(self, request, context):
        i=0
        for x in range(0, 1000):
            for z in range(0,1000):
                i = i+x+z
        return metodosgrpc_pb2.Empty()
    def MetodoTeste(self, request, context):
        i=0
        for x in range(0, 1000):
            for z in range(0,1000):
                i = i+x+z
        return metodosgrpc_pb2.Empty()
    def MetodoOitoLong(self, request, context):
        response = metodosgrpc_pb2.RespostaLong()
        response.saida = metodosgrpc.long_8_param(request.param1,request.param2,request.param3,request.param4,request.param5,request.param6,request.param7,request.param8)
        return response
    def MetodoUmParametroLong(self, request, context):
        response = metodosgrpc_pb2.RespostaLong()
        response.saida = metodosgrpc.long_1_param(request.param1)
        return response
    def MetodoUmParametroString(self, request, context):
        response = metodosgrpc_pb2.RespostaString()
        response.saida = metodosgrpc.uma_string(request.param1)
        return response
    def MetodoOitoString(self, request, context):
        response = metodosgrpc_pb2.RespostaString()
        response.saida = metodosgrpc.oito_string(request.param1,request.param2,request.param3,request.param4,request.param5,request.param6,request.param7,request.param8)
        return response
    def MetododezesseisString(self, request, context):
        response = metodosgrpc_pb2.RespostaString()
        response.saida =metodosgrpc.dezeseis_string(request.param1,request.param2,request.param3,request.param4,request.param5,request.param6,request.param7,request.param8,request.param9,request.param10,request.param11,request.param12,request.param13,request.param14,request.param15,request.param16)
        return response
    def MetodoComplexo(self, request, context):
        response = metodosgrpc_pb2.SaidaComplexo()
        i=0
        for x in range(0, 1000):
            for z in range(0,1000):
                i = i+x+z
        return response
    def MetodoVetor(self, request, context):
        response = metodosgrpc_pb2.SaidaVetor()
        response.vetor = metodosgrpc.vetor(request.vetor)
        return response
# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
metodosgrpc_pb2_grpc.add_MetodosDSIDServicer_to_server(
        MetodosDSIDServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)