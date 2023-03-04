from flask import Blueprint, request, jsonify


analysis_bp = Blueprint(
    'analysis_bp', __name__,
)

@analysis_bp.route('', methods=["POST"])
def addUser():
    try:
        pass
    except Exception as Argument:
        print(Argument)
        return Argument