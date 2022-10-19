import requests
#import json

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from rave_python import Rave, RaveExceptions

application = app = Flask(__name__)
api = Api(app)


secret_key='XXX'
public_key='XXX'



#######################  OPTION 1 - FROM SCRATCH CODING #############################

# Make Transfer
def Transfer(account_bank,account_number,amount,narration,currency,beneficiary_name):

    hed = {'Authorization': 'Bearer ' + secret_key}
    data = {
            "account_bank": account_bank,
            "account_number": account_number,
            "amount": amount,
            "narration": narration,
            "currency": narration,
            "beneficiary_name": beneficiary_name
            }

    url = 'https://api.flutterwave.com/v3/transfers'
    response = requests.post(url, json=data, headers=hed)
    return response.json()


# Check Transfer status
def checkTransferStatus(idTrans):
    hed = {'Authorization': 'Bearer ' + secret_key}
    url = 'https://api.flutterwave.com/v3/transfers/'+idTrans
    response = requests.get(url, headers=hed)
    return response.json()


#######################  OPTION 2 - USING RAVE PYTHON LIBRARY #############################    

# Make Transfer using rave
def TransferWithRave(account_bank,account_number,amount,narration,currency,beneficiary_name):

    try:
            rave = Rave(public_key, secret_key, usingEnv = False)
            res = rave.Transfer.initiate({
            "account_bank": account_bank,
            "account_number": account_number,
            "amount": amount,
            "narration": narration,
            "currency": currency,
            "beneficiary_name": beneficiary_name
            })

            return res

    except RaveExceptions.IncompletePaymentDetailsError as e:
            return e

    except RaveExceptions.InitiateTransferError as e:
            return e.err


    except RaveExceptions.ServerError as e:
            return e.err

# Check Transfer status using rave
def checkTransferStatusWithRave(idTrans):

    try:
            rave = Rave(public_key, secret_key, usingEnv = False)
            return rave.Transfer.fetch(idTrans)


    except RaveExceptions.TransferFetchError as e:
            return e.err

    except RaveExceptions.ServerError as e:
            return e.err

#######################  ENDPOINTS #############################  

@app.route("/initiateTransfer", methods=["POST"])
def initiateTransfer():

        if (request.method == 'POST'):

                        try:

                                some_json = request.get_json(force=True)
                                #return TransferWithRave(some_json["account_bank"],some_json["account_number"],some_json["amount"],some_json["narration"],some_json["currency"],some_json["beneficiary_name"])
                                return Transfer(some_json["account_bank"],some_json["account_number"],some_json["amount"],some_json["narration"],some_json["currency"],some_json["beneficiary_name"])

                        except requests.exceptions.RequestException as e: 
                                return jsonify({'error':str(e)})

        else:
                        return jsonify({'error':"Wrong method"})


@app.route("/checkTransfer", methods=["GET"])
def checkTransfer():

        if (request.method == 'GET'):

                        try:

                                some_params = request.args
                                #return checkTransferStatusWithRave(some_params["id"])
                                return checkTransferStatus(some_params["id"])
                        except requests.exceptions.RequestException as e: 
                                return jsonify({'error':str(e)})

        else:
                        return jsonify({'error':"Wrong method"})





if __name__ == '__main__':
        #app.run(debug=True)
        app.run(host="0.0.0.0", port=80)