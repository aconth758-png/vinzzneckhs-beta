from flask import Flask, request, Response, send_from_directory
import json
import os

app = Flask(__name__, static_folder='static')

# ========== FULL JSON RESPONSE DARI SERVER ASLI (200 OK) ==========
FULL_RESPONSE = {
    "abhotupdate_cdn_url": "http://104.234.186.37:5000/cdn/live/ABHotUpdates/",
    "abhotupdate_check": "cache_res;assetindexer;SH-Gpp",
    "appstore_url": "http://play.google.com/store/apps/details?id=com.dts.freefiremax",
    "backup_appstore_url": "http://play.google.com/store/apps/details?id=com.dts.freefireth",
    "backup_cdn_url": "https://dl.cdn.freefiremobile.com/live/ABHotUpdates/",
    "billboard_bg_url": "https://dl.cdn.freefiremobile.com/common/OB23/version/Patch_Bg.png",
    "billboard_cdn_url": "https://dl.dir.freefiremobile.com/common/OB54/CSH/patchupdate/sgolzjifnmi101.ff_extend;https://dl.dir.freefiremobile.com/common/OB54/CSH/patchupdate/sgolzjifnmi102.ff_extend;https://dl.dir.freefiremobile.com/common/OB54/CSH/patchupdate/sgolzjifnmi103.ff_extend;https://dl.dir.freefiremobile.com/common/OB54/CSH/patchupdate/sgolzjifnmi104.ff_extend;https://dl.dir.freefiremobile.com/common/OB54/CSH/patchupdate/sgolzjifnmi105.ff_extend;https://dl.dir.freefiremobile.com/common/OB54/CSH/patchupdate/sgolzjifnmi106.ff_extend;https://dl.dir.freefiremobile.com/common/OB54/CSH/patchupdate/sgolzjifnmi107.ff_extend",
    "billboard_msg": "",
    "cdn_url": "https://dl.cdn.freefiremobile.com/live/ABHotUpdates/",
    "client_ip": "114.10.135.175",
    "code": 0,
    "core_ip_list": ["0.0.0.0", "50.109.27.134", "129.226.2.163", "129.226.1.13", "129.226.1.16"],
    "core_url": "csoversea.castle.freefiremobile.com",
    "country_code": "BR",
    "force_refresh_restype": "optionalavatarres",
    "gamevar": "var_name,comment,var_type,var_value,var_region,var_platform\nvar_name,comment,var_type,var_value,var_region,var_platform\nEnableVariableFFVoiceIDC,EnableVariableFFVoiceIDC,bool,false,,\nEnableAccelerationOnFalling,EnableAccelerationOnFalling,bool,false,,\nEnableLowFallingSwapWeapon,EnableLowFallingSwapWeapon,bool,true,,",
    "garena_hint": False,
    "garena_login": False,
    "gdpr_version": 0,
    "ggp_url": "na-gin.freefiremobile.com",
    "gop_url": "",
    "img_cdn_url": "https://dl.cdn.freefiremobile.com/common/",
    "is_firewall_open": False,
    "is_review_server": False,
    "is_server_open": True,
    "latest_release_version": "OB54",
    "login_download_optionalpack": "optionalclothres:shaders|optionalpetres:optionalpetres_commonab_shader|optionallobbyres:",
    "login_failed_count": 2,
    "max_store": "",
    "max_video": "",
    "max_web": "",
    "min_hint_size": 1,
    "multi_region": "",
    "need_check_ip_list": [],
    "need_track_hotupdate": True,
    "network_log_server": "https://sgnetwork.ggblueshark.com/",
    "patchnote_url": "https://dl.dir.freefiremobile.com/common/web_event/aswqooiwd/zClWsKYO.html?lang=en",
    "remote_option_version": "optionallocres:49|optionalavatarres:674|optionalclothres:1107|optionalfootballres:47|optionalfullscreencgres:334|optionalhuntinggroundres:178|optionalinfection:121|optionalingameres:469|optionallobbyres:582|optionallonewolfres:77|optionallonewolfstrikeoutres:23|optionalludores:40|optionalmap1res:385|optionalmap2res:125|optionalmap4res:110|optionalmaphippores:88|optionalmapres:340|optionalnewblast:138|optionalpetres:809|optionalrushb:123|optionalrushingpetsres:88|optionalsnowduelres:59|optionaltrainingres:83|optionalugcres:502|optionalvoiceres:352|optionalwerewolves:173|optionalmapponyres:200|optionalsocialres:111|optionalwerunres:83|optionalugcoldparadiseres:32|optionalmultiregionres:25",
    "remote_option_version_astc": "optionallocres:49|optionalavatarres:677|optionalclothres:1107|optionalfootballres:38|optionalfullscreencgres:318|optionalhuntinggroundres:178|optionalinfection:116|optionalingameres:438|optionallobbyres:564|optionallonewolfres:139|optionallonewolfstrikeoutres:96|optionalludores:144|optionalmap1res:385|optionalmap2res:159|optionalmap4res:144|optionalmaphippores:89|optionalmapres:374|optionalnewblast:138|optionalpetres:809|optionalrushb:227|optionalrushingpetsres:192|optionalsnowduelres:59|optionaltrainingres:79|optionalugcres:472|optionalvoiceres:385|optionalwerewolves:277|optionalmapponyres:200|optionalsocialres:106|optionalwerunres:74|optionalugcoldparadiseres:32|optionalmultiregionres:26",
    "remote_version": "1.126.3",
    "server_url": "https://loginbp.ggpolarbear.com/",
    "should_check_ab_load": False,
    "space_required_in_GB": 1.48,
    "test_url": "",
    "use_background_download": False,
    "use_background_download_lobby": False,
    "use_login_optional_download": True,
    "web_log_server": "https://networkselftest.ff.garena.com/api/",
    "web_url": ""
}

# ========== ENDPOINT MENU UTAMA ==========
@app.route('/', methods=['GET'])
def menu():
    return send_from_directory('static', 'index.html')

# ========== ENDPOINT NECK HS ==========
@app.route('/neckhs', methods=['GET', 'POST', 'OPTIONS'])
def neck_hs():
    if request.method == 'OPTIONS':
        resp = Response()
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = '*'
        return resp

    response_data = {
        "status": "success",
        "feature": "Neck HS",
        "message": "Neck HS Activated — VINZZ MODZ",
        "code": 0
    }
    resp = json.dumps(response_data)
    return Response(resp, status=200, mimetype='application/json', headers={'Access-Control-Allow-Origin': '*'})

# ========== ENDPOINT BACK JUMP ==========
@app.route('/backjump', methods=['GET', 'POST', 'OPTIONS'])
def back_jump():
    if request.method == 'OPTIONS':
        resp = Response()
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = '*'
        return resp

    response_data = {
        "status": "success",
        "feature": "Back Jump",
        "message": "Back Jump Activated — VINZZ MODZ",
        "code": 0
    }
    resp = json.dumps(response_data)
    return Response(resp, status=200, mimetype='application/json', headers={'Access-Control-Allow-Origin': '*'})

# ========== ENDPOINT PROXYXYZ (TETAP JALAN) ==========
@app.route('/proxyxyz/<path:path>', methods=['GET', 'POST', 'OPTIONS'])
@app.route('/proxyxyz/', methods=['GET', 'POST', 'OPTIONS'])
def proxyxyz(path=''):
    if request.method == 'OPTIONS':
        resp = Response()
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = '*'
        return resp

    resp = json.dumps(FULL_RESPONSE)
    return Response(resp, status=200, mimetype='application/json', headers={'Access-Control-Allow-Origin': '*'})

# ========== FALLBACK ==========
@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(port=5000)
