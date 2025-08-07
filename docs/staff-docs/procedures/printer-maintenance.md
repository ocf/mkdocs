# Printer Maintenance

## General Information

* As of Fall 2023, we use Quill.com for our paper. See [purchase request](https://callink.berkeley.edu/finance/ocf/requests/purchase/1375196) for last membership renewal.


## Toner Cartridge Disposal

* \


## FAQ

### **Nothing shows when clicking print.**

Check what print jobs are currently lined up. Delete duplicates.

### **Pagefault isn't printing.**

cope

### **The screen above the printer isn't correct.**

Restart printhost (which runs on old kube) with the following command:

```bash
kubectl -n app-printlist rollout restart deploy/deployment
```

### **~~Page comes out completely black.~~**

~~Make sure they have the file saved as a PDF, and open it in Okular. Click print, then to go to options, PDF options, and check the box for "Force rasterization". Try printing again now.~~

No longer an issue as of Fall 2023. Turned on force rasterize by default.