_______ json
____ contextlib _______ suppress
____ dataclasses _______ dataclass
____ ipaddress _______ AddressValueError, IPv4Address, IPv4Network
____ pathlib _______ Path
____ typing _______ List


@dataclass(frozen=True)
class ServiceIPRange:
    """
    Represents an IPv4 public network range, allocated by AWS for use with
    a specific service and region.
    """

    service: s..
    region: s..
    cidr: IPv4Network

    ___ __str__(self):
        r.. (f"{self.cidr} is allocated to the {self.service} "
                f"service in the {self.region} region")


___ parse_ipv4_service_ranges(source: Path) -> List[ServiceIPRange]:
    """
    Given a JSON file containing AWS public IP addresses, return a list of
    ServiceIPRange objects representing all IPv4 network ranges. See also:

    https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
    """
    data = json.loads(source.read_text())
    with suppress(AddressValueError):
        prefixes = data["prefixes"]
        ipv4_service_ranges = [
            ServiceIPRange(
                service=prefix["service"],
                region=prefix["region"],
                cidr=IPv4Network(prefix["ip_prefix"]),
            )
            ___ prefix __ prefixes
        ]
    r.. ipv4_service_ranges


___ get_aws_service_range(address: s..,
                          service_ranges: l..) -> List[ServiceIPRange]:
    """
    Return a list of ServiceIPRange objects representing all AWS public
    IP ranges that contain `address`. Raise a ValueError if `address`
    is not a valid IPv4 address.
    """
    try:
        ipv4_address = IPv4Address(address)
    except AddressValueError:
        raise ValueError("Address must be a valid IPv4 address")

    r.. [range_ ___ range_ __ service_ranges
            __ ipv4_address __ range_.cidr]