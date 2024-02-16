# coding: utf-8
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkdns.v2.region.dns_region import DnsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkdns.v2 import *


if __name__ == "__main__":
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks.
    # It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables
    # and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication.
    # Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    ak = __import__('os').getenv("CLOUD_SDK_AK")
    sk = __import__('os').getenv("CLOUD_SDK_SK")

    credentials = BasicCredentials(ak, sk)

    client = DnsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(DnsRegion.value_of("cn-south-1")) \
        .build()

    try:
        request = UpdateRecordSetRequest()
        request.body = UpdateRecordSetReq(
            records=[
                "240e:3b4:38ee:1af0:3ae6:aff:fe89"
            ],
            ttl=300,
            type="AAAA",
            description="This is an ipv6 record set.",
            name="ipv6.likun.cc"
        )
        response = client.update_record_set(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
