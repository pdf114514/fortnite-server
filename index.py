from flask import Flask, Response, request, jsonify, redirect
import json
import datetime
import requests
import logging
import logging_tree
import traceback
from threading import Thread

###

config={}
config.update({'name': 'SERVER'})
config.update({'announcement': ':)'})
config.update({'season': '9'})

app=Flask('Server')
host='0.0.0.0'
port=8000

addhandlerlist=[
    'werkzeug',
    'urllib3'
    #'urllib3.connection',
    #'urllib3.connectionpool', 
    #'urllib3.poolmanager',
    #'urllib3.response'
]

#sys.setrecursionlimit(15000)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def getroot():return Response('"Ya :D"\n"@pdf114514"', mimetype='application/json')

@app.route('/favicon.ico')
def favicon():return redirect('https://fortnite-api.com/images/cosmetics/br/cid_005_athena_commando_m_default/icon.png')

@app.route('/_error')
def geterror():return None

@app.errorhandler(400)
@app.errorhandler(500)
def app_errorhandle(error):
    app.logger.error(traceback.format_exc())
    return jsonify({'message':traceback.format_exc()}), error.code

@app.errorhandler(404)
def app_errorhandle_404(error):
    #dlog('```\n404\n\n'+traceback.format_exc()+'\n```')
    return jsonify({'message':traceback.format_exc()}), error.code

def _dlog(*c):
    return requests.post('https://discord.com/api/webhooks/721137428928397372/KUbCDSg6it1oilCGroaGgE8YmFSeSd6jPPP7_hSNld7YKWfxOvztTlB4ccthxZj3zeUW', json={"content":''.join(c)})

def dlog(c):
    try:
        Thread(target=_dlog, args=(c)).start()
        return True
    except:
        return False

class logginghandler(logging.Handler):

    def __init__(self):
        logging.Handler.__init__(self)
        
    def emit(self, record):
        c=self.format(record)
        if 'discord.com' in c:return
        if '404' in c or '500' in c:dlog(f'```diff\n- {c}```')
        else:dlog(f'``{c}``')
        
def handle(name):
    log=logging.getLogger(name)
    if log.handlers:
        for i in log.handlers:
            log.removeHandler(i)
    hdlr=logginghandler()
    hdlr.setLevel(10)
    log.setLevel(10)
    log.addHandler(hdlr)

for i in addhandlerlist:
    handle(i)

hdlr=logginghandler()
hdlr.setLevel(10)
app.logger.setLevel(10)
app.logger.addHandler(hdlr)

#urllib3log=logging.getLogger('urllib3.connection')
#urllib3log.setLevel(10)
#hdlr=logginghandler()
#hdlr.setLevel(10)
#urllib3log.removeHandler(urllib3log.handlers[0])
#urllib3log.addHandler(hdlr)

logging_tree.printout()

requests.post('https://discordapp.com/api/webhooks/721137428928397372/KUbCDSg6it1oilCGroaGgE8YmFSeSd6jPPP7_hSNld7YKWfxOvztTlB4ccthxZj3zeUW', json={'content':'-----\nStarting...\n*****'})
###

def news():
    with open('config/news.json', 'r') as f:
        newsfile=json.load(f)
    return {
        '_title': 'Fortnite Game',
        '_activeDate': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
        'lastModified': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
        '_locale': 'en-US',
        'loginmessage': {
            '_title': 'LoginMessage',
            'loginmessage': {
                '_type': 'CommonUI Simple Message',
                'message': {
                    '_type': 'CommonUI Simple Message Base',
                    'title': 'Hello!',
                    'body': 'Hello World!'
                }
            },
            '_activeDate': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
            'lastModified': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
            '_locale': 'en-US'
        },
        'battleroyalenews': {
            'news': {
                'platform_messages': [],
                '_type': 'Battle Royale News',
                'messages': [
                    {
                        'image': newsfile[0]['image'],
                        'hidden': False,
                        '_type': 'CommonUI Simple Message Base',
                        'adspace': newsfile[0]['adspace'],
                        'title': newsfile[0]['title'],
                        'body': newsfile[0]['text'],
                        'spotlight': False
                    },
                    {
                        'image': newsfile[1]['image'],
                        'hidden': False,
                        '_type': 'CommonUI Simple Message Base',
                        'adspace': newsfile[1]['adspace'],
                        'title': newsfile[1]['title'],
                        'body': newsfile[1]['text'],
                        'spotlight': False
                    },
                    {
                        'image': newsfile[2]['image'],
                        'hidden': False,
                        '_type': 'CommonUI Simple Message Base',
                        'adspace': newsfile[2]['adspace'],
                        'title': newsfile[2]['title'],
                        'body': newsfile[2]['text'],
                        'spotlight': False
                    }
                ]
            },
            '_title': 'battleroyalenews',
            'header': '',
            'style': 'None',
            '_activeDate': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
            'lastModified': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
            '_locale': 'en-US'
        },
        'emergencynotice': {
            'news': {
                'platform_messages': [],
                '_type': 'Battle Royale News',
                'messages': [
                    {
                        'hidden': False,
                        '_type': 'CommonUI Simple Message Base',
                        'subgame': 'br',
                        'title': 'Server',
                        'body': config['announcement'],
                        'spotlight': True
                    }
                ]
            },
            '_title': 'emergencynotice',
            '_activeDate': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
            'lastModified': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
            '_locale': 'en-US'
        }
    }

def timeline():
        {
            'channels': {
                'client-matchmaking': {
                    'states': [],
                    'cacheExpire': '9999-12-31T23:59:59.999Z'
                },
            'tk': {
                'states': [
                    {
                        'validFrom': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
                        'activeEvents': [],
                        'state': {
                            'k': [
                                '001B8CDAE8386ACB5DFE26FA59C10B40:XA9kqeHyWLK/xsRzYLCkooN/dBRNTyjy5sw9Jv+8nRs=',
                                '03FBE2522823B14E3BD161BBCDAE4A85:kvHfxKURiw97DzzEt5xAUxVMFfxGya3Xw3kI7ORGEgM=',
                                'A6855B699FE10FE50301AFE1A4FA74CB:fKXFbKW6dUWHLSC8M4KLAg1elVXH+wYouFbpvvtiIcY=',
                                '82669F5A2F9B703D1A6BEA3BCB922D7D:Leu9rrDPaqZd3izIU+IKpFcP/NNcqSncLkV2lapQL6k=',
                                '3AC281E7A5EAA2765CFE02AC98B04FC8:R/hWNn8BcRRovJE/L7h15VDrJ0H4VqBBVt6XVvq2Ebw=',
                                '79F7D9C856E8CF354109D3298F076C06:Ak3TOM0i0Mq/KYxd7SDlSuS7o55USaf+urL6WqnmalY='
                            ]
                        }
                    }
                ],
                'cacheExpire': '9999-12-31T23:59:59.999Z'
            },
            'community-votes': {
                'states': [
                    {
                        'validFrom': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
                        'activeEvents': [],
                        'state': {
                            'electionId': '',
                            'candidates': [],
                            'electionEnds': '9999-12-31T23:59:59.999Z',
                            'numWinners': 1
                            }
                    }
                ],
                'cacheExpire': '9999-12-31T23:59:59.999Z'
            },
            'client-events': {
                'states': [
                    {
                        'validFrom': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
                        'activeEvents': [
                            {
                                'eventType': 'EventFlag.Season9',
                                'activeUntil': '9999-12-31T23:59:59.999Z',
                                'activeSince': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") 
                            },
                            {
                                'eventType': 'EventFlag.Season9.Phase1',
                                'activeUntil': '9999-12-31T23:59:59.999Z',
                                'activeSince': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") 
                            },
                            {
                                'eventType': 'EventFlag.LobbySeason{config["season"]}',
                                'activeUntil': '9999-12-31T23:59:59.999Z',
                                'activeSince': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") 
                            },
                            {
                                'eventType': 'EventFlag.Season9.Phase2',
                                'activeUntil': '9999-12-31T23:59:59.999Z',
                                'activeSince': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") 
                            },
                        ],  
                        'state': {
                            'activeStorefronts': [],
                            'eventNamedWeights': {},
                            'activeEvents': [
                                {
                                    'instanceId': '1gjvo0jkfchv90s38mh0limpm2[2]0',
                                    'devName': f'LobbySeason{config["season"]}',
                                    'eventName': f'LobbySeason{config["season"]}',
                                    'eventStart': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
                                    'eventEnd': '9999-12-31T23:59:59.999Z',
                                    'eventType': 'EventFlag.LobbySeason{config["season"]}'
                                }
                            ],
                            'seasonNumber': config["season"],
                            'seasonTemplateId': f'AthenaSeason:athenaseason{config["season"]}',
                            'matchXpBonusPoints': 0,
                            'seasonBegin': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
                            'seasonEnd': '9999-12-31T23:59:59.999Z',
                            'seasonDisplayedEnd': '9999-12-31T23:59:59.999Z',
                            'weeklyStoreEnd': '9999-12-31T23:59:59.999Z',
                            'stwEventStoreEnd': '9999-12-31T23:59:59.999Z',
                            'stwWeeklyStoreEnd': '9999-12-31T23:59:59.999Z',
                            'dailyStoreEnd': '9999-12-31T23:59:59.999Z'
                        }
                    }
                ],
                'cacheExpire': '9999-12-31T23:59:59.999Z'
            }
        },
        'eventsTimeOffsetHrs': 0,
        'cacheIntervalMins': 15,
        'currentTime': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") 
    }

def shop():
    with open('config/shop.json') as f:
        shopfile=json.load(f)
    r = {
        "refreshIntervalHrs": 24,
        "dailyPurchaseHrs": 24,
        "expiration": "9999-12-31T23:59:59.999Z",
        "storefronts": [
            {
                "name": "BRDailyStorefront",
                "catalogEntries": [
                    
                ]
            },
            {
                "name": "BRWeeklyStorefront",
                "catalogEntries": [
                    
                ]
            }
        ]
    }

    for i in shopfile['dailys']:
        r['storefronts'][0]['catalogEntries'].append({
                        "devName": i['id'],
                        "offerId": "v2:/7f16a118-fc18-4d8d-9712-34185db5d177",
                        "fulfillmentIds": [],
                        "dailyLimit": -1,
                        "weeklyLimit": -1,
                        "monthlyLimit": -1,
                        "categories": [],
                        "prices": [
                            {
                                "currencyType": "MtxCurrency",
                                "currencySubType": "",
                                "regularPrice": 9999,
                                "finalPrice": i['price'],
                                "saleExpiration": "9999-12-31T23:59:59.999Z",
                                "basePrice": 9999
                            }
                        ],
                        "matchFilter": "",
                        "filterWeight": 0,
                        "appStoreId": [],
                        "requirements": [
                            {
                                "requirementType": "DenyOnItemOwnership",
                                "requiredId": i['id'],
                                "minQuantity": 1
                            }
                        ],
                        "offerType": "StaticPrice",
                        "giftInfo": {
                            "bIsEnabled": False,
                            "forcedGiftBoxTemplateId": "",
                            "purchaseRequirements": [],
                            "giftRecordIds": []
                        },
                        "refundable": True,
                        "metaInfo": [],
                        "displayAssetPath": "",
                        "itemGrants": [
                            {
                                "templateId": i['id'],
                                "quantity": 1
                            }
                        ],
                        "sortPriority": 0,
                        "catalogGroupPriority": 0
                    })

    for i in shopfile['featureds']:
        r['storefronts'][1]['catalogEntries'].append({
                        "devName": i['id'],
                        "offerId": "v2:/32fb86e1-4a02-4478-935d-47f3fe333e7f",
                        "fulfillmentIds": [],
                        "dailyLimit": -1,
                        "weeklyLimit": -1,
                        "monthlyLimit": -1,
                        "categories": [],
                        "prices": [
                            {
                                "currencyType": "MtxCurrency",
                                "currencySubType": "",
                                "regularPrice": 0,
                                "finalPrice": i['price'],
                                "saleExpiration": "9999-12-31T23:59:59.999Z",
                                "basePrice": 0
                            }
                        ],
                        "matchFilter": "",
                        "filterWeight": 0,
                        "appStoreId": [],
                        "requirements": [
                            {
                                "requirementType": "DenyOnItemOwnership",
                                "requiredId": i['id'],
                                "minQuantity": 1
                            }
                        ],
                        "offerType": "StaticPrice",
                        "giftInfo": {
                            "bIsEnabled": False,
                            "forcedGiftBoxTemplateId": "",
                            "purchaseRequirements": [],
                            "giftRecordIds": []
                        },
                        "refundable": True,
                        "metaInfo": [],
                        "displayAssetPath": "",
                        "itemGrants": [
                            {
                                "templateId": i['id'],
                                "quantity": 1
                            }
                        ],
                        "sortPriority": -1,
                        "catalogGroupPriority": 0
                    })

    return r
  
def epicerror(errorCode="errors.com.epicgames", errorMessage=f"{0}, {1}, {2}", formatArgs=["Epic", "Error", "Fuck"], numericErrorCode=0, Status=400, originatingService="fortnite", intent="prod-live"):
    r=Response(status=Status, response=json.dumps({"errorCode":errorCode, "errorMessage":errorMessage, "messageVars":formatArgs, "numericErrorCode":numericErrorCode, "originatingService":originatingService, "intent":intent}))
    r.headers['X-Epic-Error-Code']=numericErrorCode
    r.headers['X-Epic-Error-Name']=errorCode
    return r

class ProfileClass():
    
    def readprofile(accid, profileid):
        with open(f'config/{accid}/profiles/profile_{profileid}.json', 'r', encoding='utf-8') as f:
            r=json.load(f)
        return r
      
    def modifystat(profile, statname, statvalue, profilechanges):
        app.logger.info('call modifystat')
        if not statname or not statvalue:return False
        
        profile['stats']['attributes'][statname] = statvalue
        
        
        profilechanges.append({"changeType": "statModified", "name": statname, "value": statvalue })
            
        app.logger.info('modifystat sucses')
        return True

    def changeitemattr(profile, itemid, attrname, attrvalue, profilechanges):
        if not itemid in profile['items']:return False
        
        item=profile['items'][itemid]
        if not item.get('attributes'):
            item['attributes'] = {}
            
        elif item['attributes'].get(attrname) == attrvalue:return False
        
        item['attributes'][attrname] = attrvalue
        
        profilechanges.append({"changeType": "itemAttrChanged", "itemId": itemid, "attributeName": attrname, "attributeValue": attrvalue })
            
        return True

    def removeitem(profile, itemid, profilechanges):
        if not itemid in profile['items']:return False
        
        profilechanges.append({"changeType": "itemRemoved", "itemId": itemid })
            
        return True

    def bumprvn(profile):
        profile.update({'rvn':profile['rvn']+1, 'updated':datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"), 'commandRevision':profile['commandRevision']+1})
        return profile

    def saveprofile(accid, profileid, data):
        with open(f'config/{accid}/profiles/profile_{profileid}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent='\t')
        return True

@app.route('/fortnite/api/game/v2/tryPlayOnPlatform/account/<accid>', methods=["POST"])
def post1(accid):
    return Response(response="true", status=200, mimetype="text/plain")

@app.route('/fortnite/api/game/v2/privacy/account/<accid>', methods=["GET"])
def get2(accid):
    return jsonify({"accountId": accid, "optOutOfPublicLeaderboards": False})

@app.route('/waitingroom/api/waitingroom', methods=["GET"])
def get3():
    return Response(status=204)

@app.route('/fortnite/api/game/v2/grant_access/<accid>', methods=["POST"])
def post4(accid):
    return Response(status=204)

@app.route('/fortnite/api/game/v2/enabled_features', methods=["GET"])
def get5():
    return jsonify([])

@app.route('/lightswitch/api/service/bulk/status', methods=["GET"])
def get6():
    return jsonify([{
			"serviceInstanceId": "fortnite",
			"status": "UP",
			"message": "OY BRUV U CANT PLAY YET",
			"maintenanceUri": None,
			"overrideCatalogIds": ["a7f138b2e51945ffbfdacc1af0541053"],
			"allowedActions": ["PLAY", "DOWNLOAD"],
			"banned": False,
			"launcherInfoDTO": {
				"appName": "Fortnite",
				"catalogItemId": "4fe75bbc5a674f4f9b356b5c90567da5",
				"namespace": "fn"
			}
		}])

@app.route('/account/api/public/account', methods=["GET"])
def get7():
    return jsonify([
			{
				'id': 'aabbccddeeff11223344556677889900',
				'displayName': config['name'],
				'externalAuths': {}
			}
		])

@app.route('/account/api/public/account/<accid>', methods=["GET"])
def get8(accid):
    return jsonify({
			'id': accid,
			'displayName': config['name'],
			'name': 'John',
			'lastName': 'Doe',
			'email': 'Jonsey@downloadmoreram.com',
			'failedLoginAttempts': 0,
			'lastLogin': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") ,
			'numberOfDisplayNameChanges': 0,
			'ageGroup': 'UNKNOWN',
			'headless': False,
			'country': 'US',
			'preferredLanguage': 'en',
			'tfaEnabled': False
		})

@app.route('/fortnite/api/v2/versioncheck/<v>', methods=["GET"])
def get9(v):
    return Response(status=204)

@app.route('/account/api/public/account/<accid>/externalAuths', methods=["GET"])
def get10(accid):
    return jsonify([])

@app.route('/account/api/oauth/verify', methods=["GET"])
def get11():
    return jsonify({
			'token': 'eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJmb3J0bml0ZSIsInN1YiI6IjMxZWU3NmFiMzFlNzQ5NzhhMDExYzRlYWRjMDlkYjRiIiwiZHZpZCI6IjVkY2FiNWRiZTg2YTczNDRiMDYxYmE1N2NkYjMzYzRmIiwibXZlciI6ZmFsc2UsImNsaWQiOiJlYzY4NGI4YzY4N2Y0NzlmYWRlYTNjYjJhZDgzZjVjNiIsImFtIjoiZXhjaGFuZ2VfY29kZSIsInAiOiJlTnF0VnR0dTRqQVFcL1IrRXF0Sm1hV3VKQjlTV1ZTVlczVjMyWWRcL1FZRStDRjhlT2JJZlN2OStKU1NDVVMwTHBVeTYyNTNMbXpCbkh4bm90UFRLdVRDNmNOeFlTWk83ZGVVelpDTUhuRnNXTFU2QkZkQ1hEYzlEcmQzT0hkaXlkWjNGMVwvcmFIZU5lSEdUM3Zvb2U3ZTdqdTlYaUVJUGoxZzVoRnM4Rk5kN00zc3lhV3F2a002d3g2MzdyQXVjbTFaMWsrVTVLejZyTkRGakZYNEMzd2hkUkp0UzZreXhTOFEySVJVNlNOTFNMTDBEcWpnVG4wbmt5NWpaUEdzeFJmZkFKQ3NuMGtmRng1dEJyVU1QZHp0MnNHRkdvQnRzaFBlK2xWU0tObXlac0ZhbWI4SE8wRW5aTkd1NUd4d1wvWHFvNUxGN3Z1dHZaVDJRRklnOVBsc01vdVwvVVNFNG5JUzhSbFErVjVUVWtqZmhXbGwyaGt0UUxBUHIzNHZ2OHpuRU9xY1lRZUdzMGl5aklnWk1hSE56VkJ0VEJxZ09SVkdtNGVVTkUwaVJXWkJxV3RxYmVza1g2QWZSRVlpS2ROb3d1dFlIMWN2VUdsVllDNVdqXC9BaHRoNW9qRzVVYm5sZisxN0Fzd0I5MHZrMHhtUUxuWDdXU0d1cytVXC9COG5rTG9tQzFTXC80elViZUM2SlBVMU15ZGxpXC8yZG1kV3J4aXNIeXgzYVdTeTZ0emxpcVplME9IZzRweXNtYUplU1k3MDUxdTRZTGd2byt5ZDcrWU1jOW1weStIV3dcL0FCZVFlTFcwVXJ0UEJBWjZwQmM3T2JsZGJLSGZIUEt0NGRTUGxpZUx3MzI1eVRhQzVZdzhhN3VKZndJampOTHFLRW14YU9cL2M2RG9tWWxqY2hzV2prd042cmlNR05OaWp0MXVwa1hKUEhlZXJxNERYWUMwcHNYSmFNUHYxdDVJOEQwSThIQ0dQcTkxOVRPS3ZKTmIrMUh6NGVBaDdqMmhrQnc4aXFKdDBYNG5RYjZTV241dHY0Mmx6bGNWdTQ2TWFtWE1JczgyRVwvdEZYTVp1T2syaXZIQXMxblZEYjhZcWNWRDl4M0o1cWVwZmpOTlFDMnVrMk92RFE5M2ZhTHJVN3B2cVN1QVJVc2QwUUtUXC9zYjFLK0xlN0UydnlMR3l2QUhyQzVaaUk0bllVXC9FQmt0VHRVTmVcLzVISFNDZjRyWjhXZ0U3dVRXOXBwNkxwT2ZnemJ0Y2JrNGhMRTE0U1p6MGw1bkM4WU1kRVhYYzI3Z0ZcL09oSWtMRjVEYmVQeEZ5dnp0VGhpK0NLRFdYZ2E1bXVhS1NxWER2TDMzd1VOWnp4dHpOZHN6OUI1MHlqKzQ9IiwiaWFpIjoiMzFlZTc2YWIzMWU3NDk3OGEwMTFjNGVhZGMwOWRiNGIiLCJjbHN2YyI6ImZvcnRuaXRlIiwidCI6InMiLCJpYyI6dHJ1ZSwiZXhwIjoxNTcyMjM2MTc4LCJpYXQiOjE1NzIyMDczNzgsImp0aSI6IjFlMmNlOWMyMDk1YTRmYzg4MmExOTA0NzU3ODdhYjFhIn0.AXL4NHObBicgMkRdeTDrAtrZx2PKoXJRkiXUV8DPIPrzZBsepEet7hfIDuahXiEPkk92SfMGv9e49WSx9s-8e1h5',
			'session_id': '1e2ce9c2095a4fc882a190475787ab1a',
			'token_type': 'bearer',
			'client_id': 'ec684b8c687f479fadea3cb2ad83f5c6',
			'internal_client': True,
			'client_service': 'fortnite',
			'account_id': 'aabbccddeeff11223344556677889900',
			'expires_in': 28739,
			'expires_at': '2019-10-28T04:16:17.845Z',
			'app': 'fortnite',
			'in_app_id': 'aabbccddeeff11223344556677889900',
			'device_id': '5dcab5dbe86a7344b061ba57cdb33c4f'
		})

@app.route('/account/api/oauth/sessions/kill', methods=["DELETE"])
def delete12():
    return Response(status=204)

@app.route('/account/api/oauth/sessions/kill/<token>', methods=["DELETE"])
def delete13(token):
    return Response(status=204)

@app.route('/account/api/oauth/token', methods=["POST"])
def post14():
    return jsonify({
			'access_token': 'eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJwIjoiZU5xVlVzbHVBakVNXC9SK0VrS0RMd2RKY3VsRDEzQTlBbm93eldHU2NVZXhBK2Z0bUVGQ0VXTVFwanRmM25xM1JNUVl3d2s1QkZMeFVyMk1ma3drYmdRc3hOMm94WVV1Z1d6WHFZRTVvT1ZIenJRR2xlWjd3N3EybUQ1VTluWlE1TkF5eEJWMWlpVVAwbnBKV3MzR2RPVFFzUHNMTzZsRFlreHBnMzhOOFArbzlpcEhZMjVDZ0VMQ21BS05TR3pDTFcxS0NKbTRrUkd4Z2RMbW01S0p6TVl0Qm4rdkFEdmJmYW5xYnp3YzFYSkJUODBOcFRlbFRXaGFhc1BCQUNiM253Q1Y2Ykhwd25NeUxtRzBKOUd1TG5iR2hGanVDaEJ3V1Nxb2NaV0hzVm1UVnkyMG9BK0ZiQ1NWTU9hQWxkQ3VXbzlERlUrVEVOaEYxUlk4N1RjNEpmeFd3Qjdwbkc3eThnTUJydWd2MTdFeW1KMmVpWlN3N1lpbVl4ZEVWVW9tMGo2SzA1S0h4OWtyV2tYUzlMVlFHcVJcL0ROZnZIOVFkWW96NEUiLCJjbHN2YyI6ImZvcnRuaXRlIiwidCI6InMiLCJtdmVyIjpmYWxzZSwiY2xpZCI6ImVjNjg0YjhjNjg3ZjQ3OWZhZGVhM2NiMmFkODNmNWM2IiwiaWMiOnRydWUsImV4cCI6MTU3MjIyMTc2MSwiYW0iOiJjbGllbnRfY3JlZGVudGlhbHMiLCJpYXQiOjE1NzIyMDczNjEsImp0aSI6IjlmZTE0YjFjZTMzNDQ2MTJhOTg4MzZhM2YxNzc1M2FhIn0.AZ7sn3F4pz1W5RaQgD4AM1prxGzwCRy-nULiegjxBjYGSCJQxphrnvNbFXyT1Izyf2nx_139PhRezevf855bu71B',
			'expires_in': 28800,
			'expires_at': '9999-12-31T23:59:59.999Z',
			'token_type': 'bearer',
			'refresh_token': 'aabbccddeeff11223344556677889900',
			'refresh_expires': 28800,
			'refresh_expires_at': '9999-12-31T23:59:59.999Z',
			'account_id': 'aabbccddeeff11223344556677889900',
			'client_id': 'ec684b8c687f479fadea3cb2ad83f5c6',
			'internal_client': True,
			'client_service': 'fortnite',
			'app': 'fortnite',
			'in_app_id': 'aabbccddeeff11223344556677889900'
		})

@app.route('/fortnite/api/receipts/v1/account/<accid>/receipts', methods=["GET"])
def get15(accid):
    return jsonify([])

@app.route('/friends/api/public/blocklist/<accid>', methods=["GET"])
def get16(accid):
    return jsonify({
			"blockedUsers": []
		})

@app.route('/friends/api/v1/<accid>/settings', methods=["GET"])
def get17(accid):
    return jsonify({
			"acceptInvites": "public"
		})

@app.route('/friends/api/public/list/fortnite/<accid>/recentPlayers', methods=["GET"])
def get18(accid):
    return jsonify([])

@app.route('/friends/api/public/friends/<accid>', methods=["GET"])
def get19(accid):
    return jsonify([
			{
				'accountId': 'aabbccddeeff11223344556677889900',
				'status': 'ACCEPTED',
				'direction': 'INBOUND',
				'created': '2018-12-06T04:46:01.296Z',
				'favorite': False
			},
			{
				'accountId': 'f926db2a84ac4c8887b26a14016c803d',
				'status': 'PENDING',
				'direction': 'INBOUND',
				'created': '2019-07-26T19:55:15.471Z',
				'favorite': False
			}
		])

@app.route('/datarouter/api/v1/public/', defaults={'path':''})
@app.route('/datarouter/api/v1/public/<path:path>', methods=["POST"])
def post20(path):
    return Response(status=204)

@app.route('/fortnite/api/cloudstorage/system', methods=["GET"])
def get21():
    return jsonify([])

@app.route('/fortnite/api/cloudstorage/user/<accid>', methods=["GET"])
def get22(accid):
    return jsonify([])

@app.route('/fortnite/api/cloudstorage/user/<accid>/<filename>', methods=["GET"])
def get23(accid, filename):
    return Response(response=json.dumps([]), status=200, mimetype="application/octet-stream")

@app.route('/fortnite/api/cloudstorage/user/<accid>/<filename>', methods=["PUT"])
def put24(accid, filename):
    return Response(status=204)

@app.route('/fortnite/api/storefront/v2/keychain', methods=['GET'])
def get25():
    return jsonify(["A93064DA8BDA456CADD2CD316BE64EE5:nziBPQTfuEl4IRK6pOaovQpqQC6nsMQZFTx+DEg62q4=:EID_FUCK_U_KID"])

@app.route('/content/api/pages/fortnite-game', methods=["GET"])
def get26():
    return jsonify(news())

@app.route('/fortnite/api/calendar/v1/timeline', methods=["GET"])
def get27():
    return jsonify(timeline())

@app.route('/fortnite/api/storefront/v2/catalog', methods=["GET"])
def get28():
    return jsonify(shop())

@app.route('/party/api/v1/Fortnite/user/<accid>', methods=["GET"])
def get29(accid):
    return jsonify({
			'current': [],
			'pending': [],
			'invites': [],
			'pings': []
		})

@app.route('/affiliate/api/public/affiliates/slug/<affname>', methods=["GET"])
def get30(affname):
    return jsonify({
            "id": "aabbccddeeff11223344556677889900",
            "slug": affname,
            "displayName": affname,
            "status": "ACTIVE",
            "verified": True,
		})

@app.route('/fortnite/api/game/v2/profile/<accid>/client/<cmd>', methods=["POST"])
def post31(accid, cmd):
  try:
    nocmd=[
        'PopulatePrerolledOffers',
        'QueryProfile',
        'RefreshExpeditions',
        'ClientQuestLogin',
        'EquipBattleRoyaleCustomization'
        ]
    profileid=request.args.get('profileId')
    profiledata=ProfileClass.readprofile(accid, profileid)
    reqjson = request.json
    
    response={
            "profileRevision": profiledata['rvn'],
            "profileId": profileid,
            "profileChangesBaseRevision": profiledata['rvn'],
            "profileChanges": [],
            "profileCommandRevision": profiledata['commandRevision'],
            "serverTime": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "responseVersion": 1
		}
    
    if cmd == 'ClientQuestLogin':
        pass
    if cmd == 'EquipBattleRoyaleCustomization':
        app.logger.info('cmd EquipBattleRoyaleCustomization '+reqjson['slotName'])
    
        cmd2 = reqjson['slotName']

        app.logger.info(cmd2)
        
        if cmd2 == 'Character':
            statname = 'favorite_character'
            statvalue = reqjson['itemToSlot']
            
        if cmd2 == 'Backpack':
            statname = 'favorite_backpack'
            statvalue = reqjson['itemToSlot']
            
        if cmd2 == 'Pickaxe':
            statname = 'favorite_pickaxe'
            statvalue = reqjson['itemToSlot']
            
        if cmd2 == 'Glider':
            statname = 'favorite_glider'
            statvalue = reqjson['itemToSlot']
            
        if cmd2 == 'SkyDiveContrail':
            statname = 'favorite_skydivecontrail'
            statvalue = reqjson['itemToSlot']
            
        if cmd2 == 'MusicPack':
            statname = 'favorite_musicpack'
            statvalue = reqjson['itemToSlot']
            
        if cmd2 == 'LoadingScreen':
            statname = 'favorite_loadingscreen'
            statvalue = reqjson['itemToSlot']
            
        if cmd2 in ['Dance', 'ItemWrap']:
            if cmd2 == 'Dance':
                statname = 'favorite_dance'
            else:
                statname = 'favorite_itemwrap'
                
            arr = profiledata['stats']['attributes'].get(statname, [])
            
            if reqjson['indexWithinSlot'] == -1:
                arr=[]
                if cmd2 == 'Dance':
                    ri = 6
                else:
                    ri = 7
                    
                for i in range(ri):
                    arr+=[reqjson['itemToSlot']]
                    
            else:
                arr[reqjson.get('indexWithinSlot', 0)] = reqjson['itemToSlot']
                
            arr2=[]
            for i in range(len(arr)):
                if not arr[i]:
                    arr2+=['']
                else:
                    arr2+=[arr[i]]
                
            statvalue = arr2
            
            
        if statname and statvalue:
            #app.logger.info(profiledata)
            app.logger.info(response['profileChanges'])
            app.logger.info(statname)
            app.logger.info(statvalue)
            app.logger.info('calling modifystat')
            ProfileClass.modifystat(profiledata, statname, statvalue, response['profileChanges'])
            #app.logger.info(profiledata)
            app.logger.info(response['profileChanges'])
            app.logger.info(statname)
            app.logger.info(statvalue)
            
    if cmd == 'MarkItemSeen':
        for i in reqjson['itemIds']:
            ProfileClass.changeitemattr(profiledata, 'item_seen', True, response['profileChanges'])
        
    if cmd == 'RemoveGiftBox':
        ProfileClass.removeitem(profiledata, reqjson['giftBoxItemId'], response['profileChanges'])
        
    if cmd == 'SetAffiliateName':
        ProfileClass.modifystat(profiledata, "mtx_affiliate", reqjson['affiliateName'], response['profileChanges'])
        
    if cmd == 'SetItemFavoriteStatus':
        ProfileClass.changeitemattr(profiledata, reqjson['targetItemId'], "favorite", reqjson['bFavorite'], response['profileChanges'])
        
    if cmd == 'SetItemFavoriteStatusBatch':
        for j, i in enumerate(reqjson['itemIds']):
            ProfileClass.changeitemattr(profiledata, i, "favorite", reqjson['itemFavStatus'][j], response['profileChanges'])
            
    if cmd == 'SetMtxPlatform':
        ProfileClass.modifystat(profiledata, "current_mtx_platform", reqjson['newPlatform'], response['profileChanges'])
        
    if cmd == 'SetReceiveGiftsEnabled':
        ProfileClass.modifystat(profiledata, "allowed_to_receive_gifts", reqjson['newPlatform'], response['profileChanges'])

    if cmd in nocmd:
        pass

    #else:
    #    return Response(status=404)
        
    if len(response['profileChanges']) > 0:
        ProfileClass.bumprvn(profiledata)
        response['profileRevision'] = profiledata['rvn']
        response['profileCommandRevision'] = profiledata['commandRevision']
        ProfileClass.saveprofile(accid, profileid, profiledata)
        
    rvn = int(request.args.get('rvn', -1))
    
    if not rvn == response['profileChangesBaseRevision']:
        response['profileChanges']=[{
                    "changeType": "fullProfileUpdate",
                    "profile": profiledata
                    }]
    
    return jsonify(response)
  except Exception as e:
    app.logger.error(e)
    return jsonify({})
  
@app.route('/fortnite/api/matchmaking/session/findPlayer/<accid>')
def get32(accid):
    return Response(status=204)
  
@app.route('/fortnite/api/game/v2/world/info')
def get33():
    return jsonify({})
  
@app.route('/fortnite/api/game/v2/twitch/<accid>')
def get34(accid):
    return jsonify({})

def main():
    app.run(host=host, port=port, threaded=True)
    
main()