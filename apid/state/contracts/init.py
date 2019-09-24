from typing import Dict, List, Any, Set, Tuple
# All clouds must enforce this contract and have these functions available

# TODO This is where 'boto' functionality is contracted


def sig_key_present(
        hub,
        name: str,
        save_private: bool = None,
        upload_public: bool = None,
        region: str = None,
        key: str = None,
        keyid: str = None,
        profile: Dict['str', object] or str = None):
    '''
    Ensure key pair is present.
    '''


def sig_key_absent(
        hub,
        name: str,
        region: str = None,
        key: str = None,
        keyid: str = None,
        profile: Dict['str', object] or str = None):
    '''
    Deletes a key pair
    '''


def sig_instance_present(
        hub,
        name: str,
        instance_name: str = None,
        instance_id: str = None,
        image_id: str = None,
        image_name: str = None,
        tags: Dict[str: str] = None,
        key_name: str = None,
        security_groups: List[str] = None,
        user_data: str = None,
        instance_type: str = None,
        placement: str = None,
        kernel_id: str = None,
        ramdisk_id: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        monitoring_enabled: bool = None,
        subnet_id: str = None,
        subnet_name: str = None,
        private_ip_address: str = None,
        block_device_map: object = None,
        disable_api_termination: bool = None,
        instance_initiated_shutdown_behavior: str = None,
        placement_group: str = None,
        client_token: str = None,
        security_group_ids: List[str] = None,
        security_group_names: List[str] = None,
        additional_info: str = None,
        tenancy: str = None,
        instance_profile_arn: str = None,
        instance_profile_name: str = None,
        ebs_optimized: bool = None,
        network_interfaces: object = None,
        network_interface_name: str = None,
        network_interface_id: str = None,
        attributes: Dict[str, object or None or bool or List[str] or Set[object]] = None,
        target_state: str = None,
        public_ip: str = None,
        allocation_id: str = None,
        allocate_eip: bool = False,
        region: str = None,
        key: str = None,
        keyid: str = None,
        profile: Dict['str', object] or str = None
):
    '''
        Ensure an EC2 instance is running with the given attributes and state.

        name
            (string) - The name of the state definition.  Recommended that this
            match the instance_name attribute (generally the FQDN of the instance).
        instance_name
            (string) - The name of the instance, generally its FQDN.  Exclusive with
            'instance_id'.
        instance_id
            (string) - The ID of the instance (if known).  Exclusive with
            'instance_name'.
        image_id
            (string) – The ID of the AMI image to run.
        image_name
            (string) – The name of the AMI image to run.
        tags
            (dict) - Tags to apply to the instance.
        key_name
            (string) – The name of the key pair with which to launch instances.
        security_groups
            (list of strings) – The names of the EC2 classic security groups with
            which to associate instances
        user_data
            (string) – The Base64-encoded MIME user data to be made available to the
            instance(s) in this reservation.
        instance_type
            (string) – The EC2 instance size/type.  Note that only certain types are
            compatible with HVM based AMIs.
        placement
            (string) – The Availability Zone to launch the instance into.
        kernel_id
            (string) – The ID of the kernel with which to launch the instances.
        ramdisk_id
            (string) – The ID of the RAM disk with which to launch the instances.
        vpc_id
            (string) - The ID of a VPC to attach the instance to.
        vpc_name
            (string) - The name of a VPC to attach the instance to.
        monitoring_enabled
            (bool) – Enable detailed CloudWatch monitoring on the instance.
        subnet_id
            (string) – The ID of the subnet within which to launch the instances for
            VPC.
        subnet_name
            (string) – The name of the subnet within which to launch the instances
            for VPC.
        private_ip_address
            (string) – If you’re using VPC, you can optionally use this parameter to
            assign the instance a specific available IP address from the subnet
            (e.g., 10.0.0.25).
        block_device_map
            (boto.ec2.blockdevicemapping.BlockDeviceMapping) – A BlockDeviceMapping
            data structure describing the EBS volumes associated with the Image.
        disable_api_termination
            (bool) – If True, the instances will be locked and will not be able to
            be terminated via the API.
        instance_initiated_shutdown_behavior
            (string) – Specifies whether the instance stops or terminates on
            instance-initiated shutdown. Valid values are:

            - 'stop'
            - 'terminate'

        placement_group
            (string) – If specified, this is the name of the placement group in
            which the instance(s) will be launched.
        client_token
            (string) – Unique, case-sensitive identifier you provide to ensure
            idempotency of the request. Maximum 64 ASCII characters.
        security_group_ids
            (list of strings) – The IDs of the VPC security groups with which to
            associate instances.
        security_group_names
            (list of strings) – The names of the VPC security groups with which to
            associate instances.
        additional_info
            (string) – Specifies additional information to make available to the
            instance(s).
        tenancy
            (string) – The tenancy of the instance you want to launch. An instance
            with a tenancy of ‘dedicated’ runs on single-tenant hardware and can
            only be launched into a VPC. Valid values are:”default” or “dedicated”.
            NOTE: To use dedicated tenancy you MUST specify a VPC subnet-ID as well.
        instance_profile_arn
            (string) – The Amazon resource name (ARN) of the IAM Instance Profile
            (IIP) to associate with the instances.
        instance_profile_name
            (string) – The name of the IAM Instance Profile (IIP) to associate with
            the instances.
        ebs_optimized
            (bool) – Whether the instance is optimized for EBS I/O. This
            optimization provides dedicated throughput to Amazon EBS and a tuned
            configuration stack to provide optimal EBS I/O performance. This
            optimization isn’t available with all instance types.
        network_interfaces
            (boto.ec2.networkinterface.NetworkInterfaceCollection) – A
            NetworkInterfaceCollection data structure containing the ENI
            specifications for the instance.
        network_interface_name
             (string) - The name of Elastic Network Interface to attach

            .. versionadded:: 2016.11.0

        network_interface_id
             (string) - The id of Elastic Network Interface to attach

            .. versionadded:: 2016.11.0

        attributes
            (dict) - Instance attributes and value to be applied to the instance.
            Available options are:

            - instanceType - A valid instance type (m1.small)
            - kernel - Kernel ID (None)
            - ramdisk - Ramdisk ID (None)
            - userData - Base64 encoded String (None)
            - disableApiTermination - Boolean (true)
            - instanceInitiatedShutdownBehavior - stop|terminate
            - blockDeviceMapping - List of strings - ie: [‘/dev/sda=false’]
            - sourceDestCheck - Boolean (true)
            - groupSet - Set of Security Groups or IDs
            - ebsOptimized - Boolean (false)
            - sriovNetSupport - String - ie: ‘simple’

        target_state
            (string) - The desired target state of the instance.  Available options
            are:

            - running
            - stopped

            Note that this option is currently UNIMPLEMENTED.
        public_ip:
            (string) - The IP of a previously allocated EIP address, which will be
            attached to the instance.  EC2 Classic instances ONLY - for VCP pass in
            an allocation_id instead.
        allocation_id:
            (string) - The ID of a previously allocated EIP address, which will be
            attached to the instance.  VPC instances ONLY - for Classic pass in
            a public_ip instead.
        allocate_eip:
            (bool) - Allocate and attach an EIP on-the-fly for this instance.  Note
            you'll want to releaase this address when terminating the instance,
            either manually or via the 'release_eip' flag to 'instance_absent'.
        region
            (string) - Region to connect to.
        key
            (string) - Secret key to be used.
        keyid
            (string) - Access key to be used.
        profile
            (variable) - A dict with region, key and keyid, or a pillar key (string)
            that contains a dict with region, key and keyid.

        .. versionadded:: 2016.3.0
        '''
    ### TODO - implement 'target_state={running, stopped}'


def instance_absent(
        hub,
        name: str,
        instance_name: str = None,
        instance_id: str = None,
        release_eip: bool = False,
        region: str = None,
        key: str = None,
        keyid: str = None,
        profile: Dict[str, Tuple[str, str]] or str = None,
        filters: Dict[str, Any] = None
):
    '''
    Ensure an EC2 instance does not exist (is stopped and removed).

    .. versionchanged:: 2016.11.0

    name
        (string) - The name of the state definition.
    instance_name
        (string) - The name of the instance.
    instance_id
        (string) - The ID of the instance.
    release_eip
        (bool)   - Release any associated EIPs during termination.
    region
        (string) - Region to connect to.
    key
        (string) - Secret key to be used.
    keyid
        (string) - Access key to be used.
    profile
        (variable) - A dict with region, key and keyid, or a pillar key (string)
        that contains a dict with region, key and keyid.
    filters
        (dict) - A dict of additional filters to use in matching the instance to
        delete.

    YAML example fragment:

    .. code-block:: yaml

        - filters:
            vpc-id: vpc-abcdef12
    '''
