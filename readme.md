git clone https://github.com/Evil-Corp/venom.git
cd venom
pip3 install aiohttp
python3 aa.py &

for i in {0..30}
do
  python3 aa.py &
done



# colab
!git clone https://github.com/Evil-Corp/venom.git
!pip3 install aiohttp
!python3 venom/aa.py