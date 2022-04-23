# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Config_pb2 as Config__pb2


class ConfigManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getConfig = channel.unary_unary(
                '/Configuration.ConfigManager/getConfig',
                request_serializer=Config__pb2.Protocolrequest.SerializeToString,
                response_deserializer=Config__pb2.ProtocolConfig.FromString,
                )
        self.setConfig = channel.unary_unary(
                '/Configuration.ConfigManager/setConfig',
                request_serializer=Config__pb2.ConfigParameters.SerializeToString,
                response_deserializer=Config__pb2.ProtocolSetting.FromString,
                )


class ConfigManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConfigManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.getConfig,
                    request_deserializer=Config__pb2.Protocolrequest.FromString,
                    response_serializer=Config__pb2.ProtocolConfig.SerializeToString,
            ),
            'setConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.setConfig,
                    request_deserializer=Config__pb2.ConfigParameters.FromString,
                    response_serializer=Config__pb2.ProtocolSetting.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Configuration.ConfigManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ConfigManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Configuration.ConfigManager/getConfig',
            Config__pb2.Protocolrequest.SerializeToString,
            Config__pb2.ProtocolConfig.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Configuration.ConfigManager/setConfig',
            Config__pb2.ConfigParameters.SerializeToString,
            Config__pb2.ProtocolSetting.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
