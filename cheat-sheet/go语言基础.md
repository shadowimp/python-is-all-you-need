## go 语言

1. go 不需要写分号

2. 定义必须调用，引用必须调用

3. 需声明变量类型

   ```go
   var num int 
   ```

   - int   整型 , int 还有int8， iny16 ， int32， int64，
   - uint 无符号整型。 
   - %p 打印地址

   ```go
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
   ```

   

4. 所有的调用必须要在主函数中

5. 打印与键盘输入语句

   ```go
   import "fmt"
   fmt.Println("")  // PrintLn 打印之后换行 ， 
   fmt.Scan()
   fmt.Scanln() // 读取一行
   ```

6. 数据类型

```go
var flag bool
flag = true 
fmt.Printf("%T,%t\n",flag,flag) // bool 类型 为 %t , %T用于查看变量类型

s1 = "shabi"
fmt.Print("%s",s1) 


// int to string 
num = 12345
num_string := strconv.Itoa(num)

// string to int 
strconv.Atoi()
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
```

1. 随机数

    ```go
    rand.Intn(10)
    ```

### Array 

```go
var nums [10] int32 
nums = append(nums, 1)  // 添加元素,nums.append(1)
l = l[:len(l)-1]  // l.pop()
```

定义数组时定义长度，默认值为0。

### 字典

```go
var map1 = map[int]int{}
```

```go
map2 = make(map[int]string)

dic := map[uint8]uint8{
        '(':')',
        '{':'}',
        '[':']',
    }
```

### 函数

需要声明，函数名 ， input类型， output类型, 函数内容

声明括号里面写input形参及变量类型， 括号外写output类型

```go
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
或者
rd := bufio.NewReader(file)

for scanner.Scan(){
  fmt.Println(strings.TrimSpace(scanner.Text))
}

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
```

### 写json

```go
dic := {}
json_str, err := json.Marshal(dic)
if err != nil{
  fmt.Println('生成json出错')
}
fmt.Println(string(json_str))

//1.Unmarshal的第一个参数是json字符串，第二个参数是接受json解析的数据结构。
//第二个参数必须是指针，否则无法接收解析的数据，如stu仍为空对象StuRead{}
//2.可以直接stu:=new(StuRead),此时的stu自身就是指针
stu:=StuRead{}
err:=json.Unmarshal(str,&stu)
```

### strings

```go
//TrimSpace， 去除字符串前后端空格。
line = strings.TrimSpace(line)

// 去掉双引号
s, _ := strconv.Unquote(string(str))
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



