from rest_framework.schemas.openapi import AutoSchema


class BaseAutoSchema(AutoSchema):
    base_name = ""

    def get_operation_id_base(self, path, method, action):
        if action == "list" and not self.base_name.endswith("s"):
            self.base_name += "s"
        return self.base_name

    def get_tags(self, path, method):
        return ["users"]


class FollowerSchema(BaseAutoSchema):
    base_name = "Follower"


class FollowingSchema(BaseAutoSchema):
    base_name = "FollowedUser"

    def get_operation_id(self, path, method):
        if method.lower() == "put":
            return "FollowUser"
        if method.lower() == "delete":
            return "UnFollowUser"
        return super().get_operation_id(path, method)

    def get_tags(self, path, method):
        return ["users"]
