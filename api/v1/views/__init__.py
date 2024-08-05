from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *  # again
from api.v1.views.states import *  # again
from api.v1.views.cities import *  # again
from api.v1.views.amenities import *  # again
from api.v1.views.users import *  # again
from api.v1.views.places import *  # again
from api.v1.views.places_reviews import *  # again
from api.v1.views.places_amenities import *  # again
