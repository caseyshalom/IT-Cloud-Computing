mosquitto_pub -h lks-iot.cimella.my.id -p 8883 --key private-key.pem --cert certificate.pem --cafile AmazonRootCA1.pem -t location/device1 -m {"hello":"test"} -i d1 -d
