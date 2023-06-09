from socket import *
# 送信側プログラム

# 送信側アドレスの設定
# 送信側IP
SrcIP = "192.168.11.57"
# 送信側ポート番号
SrcPort = 60000
# 送信側アドレスをtupleに格納
SrcAddr = (SrcIP,SrcPort)

# 受信側アドレスの設定
# 受信側IP
#DstIP = "192.168.11.38" #unity
DstIP = "192.168.11.46"  #holo
#Unityを用いるPCのIPアドレス、HoloLens2でやるときはHoloLens2のアドレス

# 受信側ポート番号
DstPort = 9000
# 受信側アドレスをtupleに格納
DstAddr = (DstIP,DstPort)

# ソケット作成
udpClntSock = socket(AF_INET, SOCK_DGRAM)
# 送信側アドレスでソケットを設定
udpClntSock.bind(SrcAddr)

# 送信データの作成
data = "send data"
# バイナリに変換
data = data.encode('utf-8')

# 受信側アドレスに送信
udpClntSock.sendto(data,DstAddr)
