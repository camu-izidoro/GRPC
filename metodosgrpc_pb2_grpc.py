# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import metodosgrpc_pb2 as metodosgrpc__pb2


class MetodosDSIDStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.MetodoVoid = channel.unary_unary(
        '/MetodosDSID/MetodoVoid',
        request_serializer=metodosgrpc__pb2.Empty.SerializeToString,
        response_deserializer=metodosgrpc__pb2.Empty.FromString,
        )
    self.MetodoTeste = channel.unary_unary(
        '/MetodosDSID/MetodoTeste',
        request_serializer=metodosgrpc__pb2.Empty.SerializeToString,
        response_deserializer=metodosgrpc__pb2.Empty.FromString,
        )
    self.MetodoUmParametroLong = channel.unary_unary(
        '/MetodosDSID/MetodoUmParametroLong',
        request_serializer=metodosgrpc__pb2.UmLong.SerializeToString,
        response_deserializer=metodosgrpc__pb2.RespostaLong.FromString,
        )
    self.MetodoOitoLong = channel.unary_unary(
        '/MetodosDSID/MetodoOitoLong',
        request_serializer=metodosgrpc__pb2.OitoLong.SerializeToString,
        response_deserializer=metodosgrpc__pb2.RespostaLong.FromString,
        )
    self.MetodoComplexo = channel.unary_unary(
        '/MetodosDSID/MetodoComplexo',
        request_serializer=metodosgrpc__pb2.Complexo.SerializeToString,
        response_deserializer=metodosgrpc__pb2.SaidaComplexo.FromString,
        )
    self.MetodoUmParametroString = channel.unary_unary(
        '/MetodosDSID/MetodoUmParametroString',
        request_serializer=metodosgrpc__pb2.UmString.SerializeToString,
        response_deserializer=metodosgrpc__pb2.RespostaString.FromString,
        )
    self.MetodoOitoString = channel.unary_unary(
        '/MetodosDSID/MetodoOitoString',
        request_serializer=metodosgrpc__pb2.OitoString.SerializeToString,
        response_deserializer=metodosgrpc__pb2.RespostaString.FromString,
        )
    self.MetododezesseisString = channel.unary_unary(
        '/MetodosDSID/MetododezesseisString',
        request_serializer=metodosgrpc__pb2.DezesseisString.SerializeToString,
        response_deserializer=metodosgrpc__pb2.RespostaString.FromString,
        )
    self.MetodoVetor = channel.unary_unary(
        '/MetodosDSID/MetodoVetor',
        request_serializer=metodosgrpc__pb2.Vetor.SerializeToString,
        response_deserializer=metodosgrpc__pb2.SaidaVetor.FromString,
        )


class MetodosDSIDServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def MetodoVoid(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetodoTeste(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetodoUmParametroLong(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetodoOitoLong(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetodoComplexo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetodoUmParametroString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetodoOitoString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetododezesseisString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetodoVetor(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MetodosDSIDServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'MetodoVoid': grpc.unary_unary_rpc_method_handler(
          servicer.MetodoVoid,
          request_deserializer=metodosgrpc__pb2.Empty.FromString,
          response_serializer=metodosgrpc__pb2.Empty.SerializeToString,
      ),
      'MetodoTeste': grpc.unary_unary_rpc_method_handler(
          servicer.MetodoTeste,
          request_deserializer=metodosgrpc__pb2.Empty.FromString,
          response_serializer=metodosgrpc__pb2.Empty.SerializeToString,
      ),
      'MetodoUmParametroLong': grpc.unary_unary_rpc_method_handler(
          servicer.MetodoUmParametroLong,
          request_deserializer=metodosgrpc__pb2.UmLong.FromString,
          response_serializer=metodosgrpc__pb2.RespostaLong.SerializeToString,
      ),
      'MetodoOitoLong': grpc.unary_unary_rpc_method_handler(
          servicer.MetodoOitoLong,
          request_deserializer=metodosgrpc__pb2.OitoLong.FromString,
          response_serializer=metodosgrpc__pb2.RespostaLong.SerializeToString,
      ),
      'MetodoComplexo': grpc.unary_unary_rpc_method_handler(
          servicer.MetodoComplexo,
          request_deserializer=metodosgrpc__pb2.Complexo.FromString,
          response_serializer=metodosgrpc__pb2.SaidaComplexo.SerializeToString,
      ),
      'MetodoUmParametroString': grpc.unary_unary_rpc_method_handler(
          servicer.MetodoUmParametroString,
          request_deserializer=metodosgrpc__pb2.UmString.FromString,
          response_serializer=metodosgrpc__pb2.RespostaString.SerializeToString,
      ),
      'MetodoOitoString': grpc.unary_unary_rpc_method_handler(
          servicer.MetodoOitoString,
          request_deserializer=metodosgrpc__pb2.OitoString.FromString,
          response_serializer=metodosgrpc__pb2.RespostaString.SerializeToString,
      ),
      'MetododezesseisString': grpc.unary_unary_rpc_method_handler(
          servicer.MetododezesseisString,
          request_deserializer=metodosgrpc__pb2.DezesseisString.FromString,
          response_serializer=metodosgrpc__pb2.RespostaString.SerializeToString,
      ),
      'MetodoVetor': grpc.unary_unary_rpc_method_handler(
          servicer.MetodoVetor,
          request_deserializer=metodosgrpc__pb2.Vetor.FromString,
          response_serializer=metodosgrpc__pb2.SaidaVetor.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MetodosDSID', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
