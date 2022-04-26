# Packages prom exporter

This Prometheus Exporter informs you about the current Yum and APT updates.

## Requirements

The exporter requires Python3 and pip3 for installation.

### Ubuntu / Debian

```shell
apt-get update && apt-get install python3 pip python3-apt git -y
```

### Red Hat based

```shell
yum install python3 pip3 git -y
```

## Installation

```shell
pip3 install git+https://github.com/centriascolocation/packages-prom-exporter.git
```

### systemd

Create this file ```/etc/systemd/system/packages-prom-exporter.service```:

```shell
[Unit]
Description=This Prometheus Exporter informs you about the current Yum and APT updates.

[Service]
ExecStart=/usr/local/bin/packages-prom-exporter

[Install]
WantedBy=multi-user.target
```

And run this command to enable und start the service:
```shell
sudo systemctl enable --now packages-prom-exporter.service
```

## Let's see


For local testing, there are two Docker files in the Docker directory.

### Ubuntu

```shell
cd Docker/ubuntu
docker build -t ubuntu20:latest .
docker run --rm -p 8000:8000 ubuntu20
```

### Amazon Linux

```shell
cd Docker/al2
docker build -t al2:latest .
docker run --rm -p 8000:8000 al2
```

### get results

```shell
➜ curl http://localhost:8000/
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 22076.0
python_gc_objects_collected_total{generation="1"} 3640.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 93.0
python_gc_collections_total{generation="1"} 8.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="7",patchlevel="10",version="3.7.10"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 3.02481408e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.8905472e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.65062351567e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.25
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP packages_updates Number of available apt updates
# TYPE packages_updates gauge
packages_updates 0.0
# HELP packeges_security_updates Number of available apt security updates
# TYPE packeges_security_updates gauge
packeges_security_updates 0.0
```