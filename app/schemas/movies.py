from marshmallow import fields, post_load, Schema, validates, ValidationError

from app.constants import CURRENT_YEAR
from app.models import Movie


class MovieSchema(Schema):
    # Fields
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    release_year = fields.Int(required=True)
    description = fields.Str(required=True)

    # Validators
    @validates("release_year")
    def validate_release_year(self, data):
        if data > CURRENT_YEAR:
            raise ValidationError("Cannot insert unreleased movie")

    # Loaders
    @post_load
    def make_user(self, data):
        return Movie(**data)


class MoviePatchSchema(Schema):
    title = fields.Str()
    release_year = fields.Int()
    description = fields.Str()


movies_list_schema = MovieSchema(many=True)
movies_item_schema = MovieSchema()
movies_patch_schema = MoviePatchSchema()