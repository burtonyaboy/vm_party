from pyVim import connect

host="[REDACTED]"
port="[REDACTED]"
user="[REDACTED]"
pwd="[REDACTED]"


try:
	my_cluster = connect.ConnectNoSSL(
		host=host,
		port=port,
		user=user,
		pwd=pwd)
	searcher = my_cluster.content.searchIndex
	vm = searcher.FindByIp(ip="[REDACTED]", vmSearch=True)
	print(vm.config.name)
except Exception as e:
	print("SOMETHING WENT WRONG LOL")
	print(e)
	exit(1)

connect.Disconnect(my_cluster)

print("lol 2 ez")