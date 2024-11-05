# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from idm_python import idm_service_pb2 as idm__python_dot_idm__service__pb2


class IDMServiceStub(object):
    """fiecare rpc are un tip de request si un tip de response
    request si response sunt mesaje (message)
    in metoda din server se va folosi request-ul pentru a extrage datele necesare
    la client se primeste tipul de response cu atributele necesare
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/IDMService/CreateUser',
                request_serializer=idm__python_dot_idm__service__pb2.UserCreateRequest.SerializeToString,
                response_deserializer=idm__python_dot_idm__service__pb2.TokenResponse.FromString,
                )
        self.Login = channel.unary_unary(
                '/IDMService/Login',
                request_serializer=idm__python_dot_idm__service__pb2.UserLoginRequest.SerializeToString,
                response_deserializer=idm__python_dot_idm__service__pb2.TokenResponse.FromString,
                )
        self.Logout = channel.unary_unary(
                '/IDMService/Logout',
                request_serializer=idm__python_dot_idm__service__pb2.TokenRequest.SerializeToString,
                response_deserializer=idm__python_dot_idm__service__pb2.StringResponse.FromString,
                )
        self.Authorize = channel.unary_unary(
                '/IDMService/Authorize',
                request_serializer=idm__python_dot_idm__service__pb2.TokenRequest.SerializeToString,
                response_deserializer=idm__python_dot_idm__service__pb2.TokenResponse.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/IDMService/DeleteUser',
                request_serializer=idm__python_dot_idm__service__pb2.DeleteRequest.SerializeToString,
                response_deserializer=idm__python_dot_idm__service__pb2.StringResponse.FromString,
                )
        self.ChangePassword = channel.unary_unary(
                '/IDMService/ChangePassword',
                request_serializer=idm__python_dot_idm__service__pb2.UserChangePasswordRequest.SerializeToString,
                response_deserializer=idm__python_dot_idm__service__pb2.TokenResponse.FromString,
                )
        self.GetUsers = channel.unary_unary(
                '/IDMService/GetUsers',
                request_serializer=idm__python_dot_idm__service__pb2.TokenRequest.SerializeToString,
                response_deserializer=idm__python_dot_idm__service__pb2.UserList.FromString,
                )


class IDMServiceServicer(object):
    """fiecare rpc are un tip de request si un tip de response
    request si response sunt mesaje (message)
    in metoda din server se va folosi request-ul pentru a extrage datele necesare
    la client se primeste tipul de response cu atributele necesare
    """

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Logout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Authorize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangePassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IDMServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=idm__python_dot_idm__service__pb2.UserCreateRequest.FromString,
                    response_serializer=idm__python_dot_idm__service__pb2.TokenResponse.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=idm__python_dot_idm__service__pb2.UserLoginRequest.FromString,
                    response_serializer=idm__python_dot_idm__service__pb2.TokenResponse.SerializeToString,
            ),
            'Logout': grpc.unary_unary_rpc_method_handler(
                    servicer.Logout,
                    request_deserializer=idm__python_dot_idm__service__pb2.TokenRequest.FromString,
                    response_serializer=idm__python_dot_idm__service__pb2.StringResponse.SerializeToString,
            ),
            'Authorize': grpc.unary_unary_rpc_method_handler(
                    servicer.Authorize,
                    request_deserializer=idm__python_dot_idm__service__pb2.TokenRequest.FromString,
                    response_serializer=idm__python_dot_idm__service__pb2.TokenResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=idm__python_dot_idm__service__pb2.DeleteRequest.FromString,
                    response_serializer=idm__python_dot_idm__service__pb2.StringResponse.SerializeToString,
            ),
            'ChangePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangePassword,
                    request_deserializer=idm__python_dot_idm__service__pb2.UserChangePasswordRequest.FromString,
                    response_serializer=idm__python_dot_idm__service__pb2.TokenResponse.SerializeToString,
            ),
            'GetUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsers,
                    request_deserializer=idm__python_dot_idm__service__pb2.TokenRequest.FromString,
                    response_serializer=idm__python_dot_idm__service__pb2.UserList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'IDMService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IDMService(object):
    """fiecare rpc are un tip de request si un tip de response
    request si response sunt mesaje (message)
    in metoda din server se va folosi request-ul pentru a extrage datele necesare
    la client se primeste tipul de response cu atributele necesare
    """

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IDMService/CreateUser',
            idm__python_dot_idm__service__pb2.UserCreateRequest.SerializeToString,
            idm__python_dot_idm__service__pb2.TokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IDMService/Login',
            idm__python_dot_idm__service__pb2.UserLoginRequest.SerializeToString,
            idm__python_dot_idm__service__pb2.TokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IDMService/Logout',
            idm__python_dot_idm__service__pb2.TokenRequest.SerializeToString,
            idm__python_dot_idm__service__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Authorize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IDMService/Authorize',
            idm__python_dot_idm__service__pb2.TokenRequest.SerializeToString,
            idm__python_dot_idm__service__pb2.TokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IDMService/DeleteUser',
            idm__python_dot_idm__service__pb2.DeleteRequest.SerializeToString,
            idm__python_dot_idm__service__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IDMService/ChangePassword',
            idm__python_dot_idm__service__pb2.UserChangePasswordRequest.SerializeToString,
            idm__python_dot_idm__service__pb2.TokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IDMService/GetUsers',
            idm__python_dot_idm__service__pb2.TokenRequest.SerializeToString,
            idm__python_dot_idm__service__pb2.UserList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)