mosquitto_pub -h lks-iot.[your.domain] -p 8883 --key private-key.pem --cert certificate.pem --cafile AmazonRootCA1.pem -t location/device1 -m {"hello":"test"} -i d1 -d
