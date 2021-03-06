from flask import Flask
import routes.BloodDonorCentre

app = Flask(__name__)
app.register_blueprint(routes.BloodDonorCentre.blueprint, url_prefix='/bloodDonorCentre')
app.run()