# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stdlib.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stdlib.proto',
  package='stdlib',
  syntax='proto3',
  serialized_pb=_b('\n\x0cstdlib.proto\x12\x06stdlib\"\x16\n\x03\x46oo\x12\x0f\n\x07message\x18\x01 \x01(\t\"$\n\x03\x42\x61r\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t22\n\x06StdLib\x12(\n\nSimpleSync\x12\x0b.stdlib.Foo\x1a\x0b.stdlib.Bar\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FOO = _descriptor.Descriptor(
  name='Foo',
  full_name='stdlib.Foo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='stdlib.Foo.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=46,
)


_BAR = _descriptor.Descriptor(
  name='Bar',
  full_name='stdlib.Bar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='stdlib.Bar.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='stdlib.Bar.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['Foo'] = _FOO
DESCRIPTOR.message_types_by_name['Bar'] = _BAR

Foo = _reflection.GeneratedProtocolMessageType('Foo', (_message.Message,), dict(
  DESCRIPTOR = _FOO,
  __module__ = 'stdlib_pb2'
  # @@protoc_insertion_point(class_scope:stdlib.Foo)
  ))
_sym_db.RegisterMessage(Foo)

Bar = _reflection.GeneratedProtocolMessageType('Bar', (_message.Message,), dict(
  DESCRIPTOR = _BAR,
  __module__ = 'stdlib_pb2'
  # @@protoc_insertion_point(class_scope:stdlib.Bar)
  ))
_sym_db.RegisterMessage(Bar)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class StdLibStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SimpleSync = channel.unary_unary(
        '/stdlib.StdLib/SimpleSync',
        request_serializer=Foo.SerializeToString,
        response_deserializer=Bar.FromString,
        )


class StdLibServicer(object):

  def SimpleSync(self, request, context):
    """NOTE is it possible to only pass int32 or none ?
    normal synchronous function call
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StdLibServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SimpleSync': grpc.unary_unary_rpc_method_handler(
          servicer.SimpleSync,
          request_deserializer=Foo.FromString,
          response_serializer=Bar.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'stdlib.StdLib', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaStdLibServicer(object):
  def SimpleSync(self, request, context):
    """NOTE is it possible to only pass int32 or none ?
    normal synchronous function call
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaStdLibStub(object):
  def SimpleSync(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """NOTE is it possible to only pass int32 or none ?
    normal synchronous function call
    """
    raise NotImplementedError()
  SimpleSync.future = None


def beta_create_StdLib_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('stdlib.StdLib', 'SimpleSync'): Foo.FromString,
  }
  response_serializers = {
    ('stdlib.StdLib', 'SimpleSync'): Bar.SerializeToString,
  }
  method_implementations = {
    ('stdlib.StdLib', 'SimpleSync'): face_utilities.unary_unary_inline(servicer.SimpleSync),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_StdLib_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('stdlib.StdLib', 'SimpleSync'): Foo.SerializeToString,
  }
  response_deserializers = {
    ('stdlib.StdLib', 'SimpleSync'): Bar.FromString,
  }
  cardinalities = {
    'SimpleSync': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'stdlib.StdLib', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
