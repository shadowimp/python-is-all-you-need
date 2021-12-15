### go 语言Basic

```
1. go 不需要写分号
2. 定义必须调用，引用必须调用
3. 需声明变量类型
所有的调用必须要在主函数中
```

### 数据类型

```go
var num int 
int 整型 , int 还有int8， iny16 ， int32， int64，
- uint 无符号整型。 
- %p 打印地址



var flag bool
flag = true 
fmt.Printf("%T,%t\n",flag,flag) // bool 类型 为 %t , %T用于查看变量类型

s1 = "shabi"
fmt.Print("%s",s1) 

//strconv库 进行 string类型与其他类型间的转换
// int to string 
num = 12345
num_string := strconv.Itoa(num)

// uint64 to string 
strconv.FormatUint()

// string to int 
strconv.Atoi()
i, err := strconv.Atoi("12345")
if err != nil {
  panic(err)
}

// string to float64
strconv.ParseFloat(arg, 64)

// float to sting 
v := 3.1415926535
s1 := strconv.FormatFloat(v, 'E', -1, 64)  // v type :float64


rand.Intn(10) //随机数

// list to string
string(result)

//  自定数据数据类型
type Stu struct {
    Name  string `json:"name"`
    Age   int
    HIgh  bool
    sex   string
    Class *Class `json:"class"`
}

type Class struct {
    Name  string
    Grade int
}

type StuRead struct {
	Name interface{}
}
data := new(StuRead)
data.Name = "nb"

// 调用
stu := Stu{
  Name: "张三",
  Age:  18,
  HIgh: true,
  sex:  "男",
}

//指针变量
c := new(Class)
c.Name = 'pony'
c.Grade = 3
stu.Class = c

// 打印变量类型
fmt.Println(reflect.TypeOf(sa))


//全局变量定义在函数外部,全局变量在任何地方都能使用
```

### 打印与键盘输入语句

```go
import "fmt"

fmt.Println("")  // PrintLn 打印之后换行 ， 

fmt.Println("hello world", "hello")	//print中可以包含多个变量以逗号隔开

fmt.Printf("number1等于:%d\n", num1)

var f1 float32
f1 = 3.1415926
fmt.Printf("%.3f\n", f1) // 三位小数print

fmt.Scan()
fmt.Scanln() // 读取一行

```

### 条件语句 ： else if

```go
if a == 1 || b==2{
  fmt.Print('a')
}

// 逻辑运算符   &&  与   ， || 或   ，  ！非
```

### 循环 语句 For

```go
for i:=1 ; i <= 5 ; i++ {
  fmt.Println(i)
}

i := 1  
for i <=5 {
  fmt.Println(i)
  i++ 
}

// 遍历字符串中的每个元素
for i := range str{
  fmt.Print(i)
}

for _, v := range nums{
  fmt.Println(v)
} 
```

### Array 数组

```go
// 定义数组，定义数组时定义长度，默认值为0。The list can't change length .
var nums [10] int32 
var numbers []float64

// 初始化数组
s := []byte{}


// 赋值
nums1 := [...]int{1,2,3,4,5} // [...] means not given the length
fmt.Println(nums1)

// l.pop()
l = l[:len(l)-1]  

// 遍历数组
for i:= 0 ;i <len(nums1); i++ {
  fmt.Println(nums1[i])
}

for _, num := range nums{
  fmt.Println(num)
}

arr1 := [4] int {1,2,3,4}
for i ,v := range arr1{
  fmt.Println(i,v)
}


// append 
nums = append(nums, 1)  // 添加元素,nums.append(1)
numbers = append(numbers, n)

// 将两个列表合并
words1 :=[] int {1,2,3,4,6,6}
words2 :=[] int {1,2,3,4,6,6}
words1 = append(words1,words2...)
```

### 字符串

```go
//TrimSpace， 去除字符串前后端空格。
line = strings.TrimSpace(line)

// 去掉双引号
s, _ := strconv.Unquote(string(str))

// 根据空格对字符串进行分割
arr:=strings.Fields(s)

// 使用指定分割
strings.Split(s, "\t")

// join
strings.Join(words, "/")

// 去掉字符串中的引号
str := "\"adf\""
s, _ := strconv.Unquote(string(str))
fmt.Println(s)

// 中文字符串的长度 ， len中文的长度为3
utf8.RuneCountInString("狗")

// 大小写转换
strings.ToLower("iPad")
strings.ToUpper("hello world")

// 判断字符串中是否包含某个字符/子串 ， 包含返回true ， 不包含返回false
strings.Contains(s, ' ')

// 字符串中包含某个字符的个数
strings.Count(s, "!")
```

### 字典

```go
var map1 = map[int]int{}
map1[2] = 3
```

```go
map2 = make(map[int]string)

dic := map[uint8]uint8{
        '(':')',
        '{':'}',
        '[':']',
    }

// 遍历字典的key
for key := range map1{
  fmt.Println(key, map1[key])
}

for key, value := range map1{
	fmt.Println(key, value)
}

// 查看key是否在字典中存在
value, ok := map1[key]
if ok{
  fmt.Println("true")
}


//map赋值前要先初始化
var words_and_tag map[string]string
words_and_tag = make(map[string]string)
words_and_tag[word] = tag
```

### 函数

需要声明，函数名 ， input类型， output类型, 函数内容

声明括号里面写input形参及变量类型， 括号外写output类型

```go
// 定义加法函数
func getSum(x1 int, x2 int)(y int){
	y = x1 + x2
	return y
}

func fun(a1 int, a2 int)int{
  b = a1+ a2
  return a1+a2
}

func max(x int , y int)int{
  if x>y{
    return x
  }else{
    return y
  }
}

// 去重
func RemoveRepeat(slc []string) []string {
	result := []string{}  // 存放结果
	for i := range slc{
		flag := true
		for j := range result{
			if slc[i] == result[j] {
				flag = false  // 存在重复元素，标识为false
				break
			}
		}
		if flag {  // 标识为false，不添加进结果
			result = append(result, slc[i])
		}
	}
	return result
}


go func() {

.....

}()

// 以并发的方式调用匿名函数func
```

### 打开文件

```go		
file, err := os.Open("test.txt")
if err != nil{
  panic(err)
}
defer file.Close()
scanner := bufio.NewScanner(file)
for scanner.Scan(){
  fmt.Println(strings.TrimSpace(scanner.Text))
}

// read file
file, err := os.Open("test.txt")
if err != nil {
  panic(err)
}
defer file.Close()
rd := bufio.NewReader(file)
for {
  line, err := rd.ReadString('\n')
  line = strings.TrimSpace(line) // 去除字符串前后空格
  fmt.Println(line)
  if err != nil || io.EOF == err {
    break
  }
  l := strings.Split(line, ":")
  fmt.Println(l)
}



// 写文件
// 先创建文件
f, err := os.Create("/Users/yuanbo6/Downloads/word_count_test.txt")
if err != nil{
  panic(err)
}
defer f.Close()

write_line := strings.Join(valid_words, " ")
write_line += "\n"
_, err = f.Write([]byte(write_line))
if err != nil{
  panic(err)
}



n, err1 := io.WriteString(f, wireteString) 
```

### defer 延迟语句 ， 在函数最后执行

1. defer 先传递参数， 最后执行
2. 常用于文件读写



### 读 json数据

golang json里的struct变量首字母需要大写的

http://xiaorui.cc/archives/2858

https://goinbigdata.com/how-to-correctly-serialize-json-string-in-golang/

```go
import "encoding/json"
// 读取json
file, err := os.Open("test.txt")
if err != nil{
  painc(err)
}
defer file.Close()
// 解码json
var map1 = map[string][string]
decoder := json.NewDecoder(file)
err = decoder.Decode(&person)
if err != nil{
  panic(err)
}else{
  fmt.Println(person)
}


json_str := `{"version": {"id": 3,"data": "2016-03-11","detail": [{"ops": "add my email"}]}}`
js, err := simplejson.NewJson([]byte(json_str)) //反序列化
if err != nil {
  fmt.Printf("%v\n", err)
  return
}
fmt.Println(js.Get("version").Get("id"))

```

```go

type Student struct {
	Name interface{}
}

data = new(Student)
data.Name = "snow"
json_str, err := json.Marshal(data)	//序列化
if err != nil{
  print('生成json出错')
}

stu = new(Student)
err = json.Unmarshal([]byte(json_str), &stu) //反序列化
if err != nil{
  fmt.Println(err)
}
fmt.Println(stu)
//1.Unmarshal的第一个参数是json字符串，第二个参数是接受json解析的数据结构。
//第二个参数必须是指针，否则无法接收解析的数据，如stu仍为空对象StuRead{}
//2.可以直接stu = new(Student),此时的stu自身就是指针

```

### 安装第三方库

```go
go get xxx // 这条命令会把远端的第三方包下载并解压到你的GOPATH路径下的src文件夹里面去，并执行go install xxx命令来安装该包,结果是在GOPATH路径的pkg文件夹生成xxx.a文件

go version

go env

// 安装 echo
mkdir -p $GOPATH/src/golang.org/x
cd $GOPATH/src/golang.org/x
git clone https://github.com/golang/net.git
git clone https://github.com/golang/sys.git
git clone https://github.com/golang/unix.git
git clone https://github.com/golang/crypto.git
git clone https://github.com/golang/text.git
```

### 数组嵌套

```go
type test struct {
	Class	int			`json:"class"`
	Person	[]person	`json:"person"`
}

type person struct {
	Name	string		`json:"name"`
	Sex		string		`json:"sex"`
}

class6 := 
`{	"class":6,
	"person":[{
		"name":"wangha",
		"sex":"male",
	},
	{
		"name":"zhang",
		"sex":"female",
	}]
}`

var keys test
if err := json.Unmarshal([]byte(class6), &keys);err != nil{
	fmt.Println(err)
}else {
	fmt.Printf("%+v\n", keys)
	fmt.Printf("%+v\n", keys.Person[1])
	fmt.Printf("%s\n", keys.Person[0].Sex)
}
```

### Goroutines

在函数或方法调用前面加上关键字go，您将会同时运行一个新的Goroutine。

```go
func hello() {  
    fmt.Println("Hello world goroutine")
}
func main() {  
    go hello() 
    fmt.Println("main function")
}
```

### channel

操作符是箭头 <-

(箭头的指向就是数据的流向)

```go
ch <- v    // 发送值v到Channel ch中
v := <-ch  // 从Channel ch中接收数据，并将数据赋值给v

// channel必须先创建再使用:
ch := make(chan int)

make(chan int, 100) //容量(capacity)代表Channel容纳的最多的元素的数量，代表Channel的缓存的大小。


```

### time

```go
now := time.Now()
day := now.Day()
hour := now.Hour()
minute := now.Minute()
second := now.Second()
fmt.Println(day)
fmt.Println(hour)
fmt.Println(minute)
fmt.Println(second)


// time.after和time.Timer需要对通道进行释放才能达到定时的效果
// 睡眠10秒
time.Sleep(time.Second * 10) 

//实现周期定时 
tiker := time.NewTicker(time.Minute) // 每隔一分钟,
for i := 0; i < 3; i++ {
  fmt.Println(<-tiker.C) //ticker.C中每隔一分钟会有一个内容加入
}


```

### 安装库

```shell
hash_code_topic.go // 打印go环境地址

// 创建文件夹
mkdir -p $GOPATH/src/golang.org/x

// 安装依赖的库
git clone https://github.com/golang/crypto.git
git clone https://github.com/golang/unix.git
git clone https://github.com/golang/text.git

// 安装 echo
go get -v -u github.com/labstack/echo
```

### 多线程

我们想在继续执行goroutine之前等待所有的goroutines执行完毕

```go
waitgroup 用来阻塞主协程，可以等待所有协程执行完

Add(n)【n为总共要等待的协程数】，
Done【在协程中调，相当于Add(-1)】
wg.Wait()  // 等待所有goroutine执行完毕

defer wg.Done() //当goroutine执行完毕前，需要告诉WaitGroup执行完毕，调用对应代码

var wg sync.WaitGroup // wg := sync.WaitGroup{}
wg.Add(1) 
go foo(wg)
fmt.Println("before wait")
wg.Wait()
fmt.Println("after wait")

func foo(wg sync.WaitGroup) {
	fmt.Println("before sleep")
	time.Sleep(2 * time.Second)
	fmt.Println("after sleep")
	wg.Done()
}


// example 2 ， 等待N个进行完成操作
func main() {
    var wg sync.WaitGroup
    for i := 0; i < 10; i++ {
        wg.Add(1)
        go func(j int) {
            fmt.Println("你好，世界" + fmt.Sprintf("%v", j))
            wg.Done()
        }(i)
    }
    wg.Wait()
}



//CPU核数
runtime.NumCPU()


```

### 标准库

os.Stat()方法用于获取文件属性

```go

func main() {
	fileInfo, err := os.Stat(`C:\Users\Administrator\Desktop\应用商店.txt`)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(fileInfo.Name())    //应用商店.txt
	fmt.Println(fileInfo.IsDir())   //false  判断是否是目录
	fmt.Println(fileInfo.ModTime()) //2019-12-05 16:59:36.8832788 +0800 CST   文件的修改时间
	fmt.Println(fileInfo.Size())    //3097  文件大小
  fmt.Println(fileInfo.Mode())    // -rw-rw-rw-  读写属性
}


```

### http

https://www.cnblogs.com/zhaof/p/11346412.html

```go	
  respond, err := http.Get("http://www.baidu.com")
  if err != nil{
    panic(err)
  }
  body, err := ioutil.ReadAll(respond.Body)
  fmt.Println(string(body))
```

自定参数变量

```go
	params := url.Values{}
	Url, err := url.Parse("http://10.41.24.195:8080/KeywordExtend/Cos")
	if err != nil {
		return
	}

	query := "蔡徐坤"
	params.Set("topn","30")
	params.Set("keywords", query)
	//如果参数中有中文参数,这个方法会进行URLEncode
	Url.RawQuery = params.Encode()
	urlPath := Url.String()
	fmt.Println(urlPath) 
	respond,err := http.Get(urlPath)
	defer respond.Body.Close()
	body, _ := ioutil.ReadAll(respond.Body)
	fmt.Println(string(body))
```



### go 在crontab里面运行报错 解决方案

直接写sh脚本 run.sh

```bash
#!/bin/sh  
cd /root/test/
go run main.go
```



### hash

```golang
package main

import (
        "fmt"
        "hash/fnv"
)

func hash(s string) uint32 {
        h := fnv.New32a()
        h.Write([]byte(s))
        return h.Sum32()
}

func main() {
        fmt.Println(hash("HelloWorld"))
        fmt.Println(hash("HelloWorld."))
}



// or 
func FNV32a(text string) uint32 {
    algorithm := fnv.New32a()
    algorithm.Write([]byte(text))
    return algorithm.Sum32()
}
```





