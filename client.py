import grpc
import time
from datetime import datetime

# import the generated classes
import metodosgrpc_pb2
import metodosgrpc_pb2_grpc

ini = time.time()
channel = grpc.insecure_channel('192.168.0.17:50051')
stub = metodosgrpc_pb2_grpc.MetodosDSIDStub(channel)
stub.MetodoTeste(metodosgrpc_pb2.Empty())
fim = time.time()
print("METODO TESTE PARA SER DESCARTADO ", fim-ini)

ini1 = time.time()
channel1 = grpc.insecure_channel('localhost:50051')
stub1 = metodosgrpc_pb2_grpc.MetodosDSIDStub(channel1)
stub1.MetodoVoid(metodosgrpc_pb2.Empty())
fim1 = time.time()
print("METODO VOID ", fim1-ini1)

ini2 = time.time()
channel2 = grpc.insecure_channel('localhost:50051')
stub2 = metodosgrpc_pb2_grpc.MetodosDSIDStub(channel2)
entrada2 = metodosgrpc_pb2.UmLong(param1=123223423) 
response2 = stub2.MetodoUmParametroLong(entrada2)
fim2 = time.time()
print("METODO COM UM LONG E RETURN  ", fim2-ini2)

ini3 = time.time()
channel3 = grpc.insecure_channel('localhost:50051')
stub3= metodosgrpc_pb2_grpc.MetodosDSIDStub(channel3)
entrada3 = metodosgrpc_pb2.OitoLong(param1=123223423,param2=123223423,param3=123223423,param4=123223423,param5=123223423,param6=123223423,param7=123223423,param8=123223423) 
response3 = stub3.MetodoOitoLong(entrada3)
fim3 = time.time()
print("METODO COM OITO LONG E RETURN", fim3-ini3)


ini5= time.time()
channel5 = grpc.insecure_channel('localhost:50051')
stub5 = metodosgrpc_pb2_grpc.MetodosDSIDStub(channel5)
entrada5 = metodosgrpc_pb2.UmString(param1='aadorq3942894jtuehfsurhwuer') 
response5 = stub5.MetodoUmParametroString(entrada5)
fim5 = time.time()
print("METODO COM UMA STRING E RETURN ", fim5-ini5)

ini6= time.time()
channel6 = grpc.insecure_channel('localhost:50051')
stub6 = metodosgrpc_pb2_grpc.MetodosDSIDStub(channel6)
entrada6 = metodosgrpc_pb2.OitoString(param1='aadorq3942894jtuehfsurhwuer',param2='aadorq3942894jtuehfsurhwuer',param3='aadorq3942894jtuehfsurhwuer',param4='aadorq3942894jtuehfsurhwuer',param5='aadorq3942894jtuehfsurhwuer',param6='aadorq3942894jtuehfsurhwuer',param7='aadorq3942894jtuehfsurhwuer',param8='aadorq3942894jtuehfsurhwuer') 
response6 = stub6.MetodoOitoString(entrada6)
fim6 = time.time()
print("METODO COM OITO STRING E RETURN ", fim6-ini6)


ini7= time.time()
channel7 = grpc.insecure_channel('localhost:50051')
stub7 = metodosgrpc_pb2_grpc.MetodosDSIDStub(channel7)
entrada7 = metodosgrpc_pb2.DezesseisString(param1='aadorq3942894jtuehfsurhwuer',param2='aadorq3942894jtuehfsurhwuer',param3='aadorq3942894jtuehfsurhwuer',param4='aadorq3942894jtuehfsurhwuer',param5='aadorq3942894jtuehfsurhwuer',param6='aadorq3942894jtuehfsurhwuer',param7='aadorq3942894jtuehfsurhwuer',param8='aadorq3942894jtuehfsurhwuer',
param9='aadorq3942894jtuehfsurhwuer',param10='aadorq3942894jtuehfsurhwuer',param11='aadorq3942894jtuehfsurhwuer',param12='aadorq3942894jtuehfsurhwuer',param13='aadorq3942894jtuehfsurhwuer',param14='aadorq3942894jtuehfsurhwuer',param15='aadorq3942894jtuehfsurhwuer',param16='aadorq3942894jtuehfsurhwuer') 
response7 = stub7.MetododezesseisString(entrada7)
fim7 = time.time()
print("METODO COM DEZESSEIS STRING E RETURN ", fim7-ini7)


ini8 = time.time()
arrayTeste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
channel8 = grpc.insecure_channel('localhost:50051')
stub8= metodosgrpc_pb2_grpc.MetodosDSIDStub(channel8)
entrada8 = metodosgrpc_pb2.Vetor(vetor=bytes(arrayTeste)) 
response8 = stub8.MetodoVetor(entrada8)
fim8 = time.time()
print("METODO COM VETOR E RETURN = ", fim8-ini8)

ini4 = time.time()
channel4 = grpc.insecure_channel('localhost:50051')
stub4= metodosgrpc_pb2_grpc.MetodosDSIDStub(channel4)
objectParameter = metodosgrpc_pb2.Objeto()
objectParameter.obj ="x"
entrada4 = metodosgrpc_pb2.Complexo(objeto=objectParameter)
response4 = stub4.MetodoComplexo(entrada4)
fim4 = time.time()
print("METODO COM COMPLEXO E RETURN ", fim4-ini4)


# et voilà
num = input("Digite x para fechar:")
print(num)