
import requests
import ipaddress

def get_ip_info(ip_address):
    try:
        ip_obj = ipaddress.ip_address(ip_address)
        version = ip_obj.version
        is_private = ip_obj.is_private
        is_global = ip_obj.is_global
        is_multicast = ip_obj.is_multicast
        is_reserved = ip_obj.is_reserved
        is_loopback = ip_obj.is_loopback
        is_link_local = ip_obj.is_link_local
        is_site_local = ip_obj.is_site_local

        print(f"IP address version: {version}")
        print(f"Is private: {is_private}")
        print(f"Is global: {is_global}")
        print(f"Is multicast: {is_multicast}")
        print(f"Is reserved: {is_reserved}")
        print(f"Is loopback: {is_loopback}")
        print(f"Is link-local: {is_link_local}")
        print(f"Is site-local: {is_site_local}")

    except ValueError:
        print("Invalid IP address format.")

# Example usage
get_ip_info( 192.0.2.1 )
