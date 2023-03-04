from flask import Blueprint

bp = Blueprint("api", __name__, url_prefix="/api")



####################################################
from pathlib import Path
import pandas as pd
DATA_PATH = Path(__file__).parent.parent.joinpath('paralympic_app')

# Loading csv prepared data into pandas dataframe:
filename = "paralympic_app/data/regions.csv"
df = pd.read_csv(filename)
####################################################

# Add the API routes to this file

from flask import request

# for a route with one method:
@bp.get('/noc')
def NOC():
    """Returns a list of NOC region codes with region name and notes """
    dff = df.values.tolist()
    return dff

# route with one method + variable rule route:
@bp.get('/noc/<code>')
def NOC_code(code):
    """returns the details for that code """
    return "Returns a specific region's name and notes with code " + str(code)


# # route with one method + variable rule route + built on previous:
# @bp.get('/noc')
# @bp.get('/noc/<code>')
# def NOC_code(code=None):
#     """Returns a list of NOC codes with the country/region name
#     and notes or if a code is passed then returns the details for
#     that code """
#     if code:
#         return "Returns a specific region's name and notes with code" + str(code)
#     else:
#         return 'Returns a list on NOC codes'


@bp.patch('/noc/<code>')
def change_field(code):
    """Return all the details of the updated NOC record"""
    return "Changed fields for the NOC record (PATCH) and returns result:" + str(code)

@bp.post('/noc')
def NOC_confirm():
    """Status code 201 if new NOC code was saved."""
    return "Status code 201 if new NOC code was saved."

@bp.delete('/noc/<code>')
def NOC_delete(code):
    """Removes an NOC code and if successful returns 202 (Accepted)"""
    return "Removes an NOC code " + code + " and if successful returns 202 (Accepted)"

# # for a route with MORE THAN one method:
# @bp.route('/noc/{code}', methods=['GET','PATCH'])
# def NOC_regions():
#     if request.method == 'GET':
#         """Returns the region name and notes for a given code"""
#         return "Returns a specific region's name and notes"
#     else:
#         """Return all the details of the updated NOC record"""
#         return 'Changed fields for the NOC record and returns result'



# for a route with MORE THAN one method:

# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method =='POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()