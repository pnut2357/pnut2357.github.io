var store = [{
        "title": "Cheatsheets",
        "excerpt":"This is a simple collection of useful commands that I plan to keep up-to-date for reference.   Use the menu on the left to browse applications.  ","categories": [],
        "tags": [],
        "url": "http://localhost:4000/cheatsheets/introduction/",
        "teaser":null},{
        "title": "Chocolatey Cheatsheet",
        "excerpt":"Useful Links Commands Reference Package Repository Installing Chocolatey Chocolatey installs in seconds. Just run the following command from an administrative PowerShell v3+ prompt (Ensure Get-ExecutionPolicy is not Restricted): Invoke-WebRequest https://chocolatey.org/install.ps1 -UseBasicParsing | Invoke-Expression List Installed Packages choco list --local-only Install a Package Standard Package Installation choco install PACKAGENAME -y choco...","categories": [],
        "tags": [],
        "url": "http://localhost:4000/cheatsheets/chocolatey/",
        "teaser":null},{
        "title": "Packer Cheatsheet",
        "excerpt":"Useful Links Documentation Installing Packer Chocolatey makes this a breeze: choco install packer -y Validate JSON Template Validate Syntax and Configuration packer validate TEMPLATENAME.json Validate Syntax Only packer validate -syntax-only TEMPLATENAME.json Debugging Enable Logging to a File This example uses PowerShell to set environmental variables: # Set timestamp and environment...","categories": [],
        "tags": [],
        "url": "http://localhost:4000/cheatsheets/packer/",
        "teaser":null},{
        "title": "Vagrant Cheatsheet",
        "excerpt":"Add a box from local path vagrant box add --name BOXNAME C:\\Packer\\Artifacts\\Path\\To\\BOXNAME.box List boxes vagrant box list Remove boxes vagrant box remove BOXNAME vagrant box remove windows_2012_r2_virtualbox Initialize the current directory to be a Vagrant environment vagrant init BOXNAME vagrant init windows_2012_r2_virtualbox Show status of current box from within it’s...","categories": [],
        "tags": [],
        "url": "http://localhost:4000/cheatsheets/vagrant/",
        "teaser":null},{
        "title": "VirtualBox Cheatsheet",
        "excerpt":"List VMs VBoxManage list vms Info: includes hidden VMs created by Vagrant Delete VM VBoxManage unregistervm VMNAME --delete Delete ALL VMs This PowerShell one-liner will get all VM names from their folder names, then delete every VM. Just update your path to where your VirtualBox VMs are stored: (Get-ChildItem 'D:\\VMs\\VirtualBox').Name...","categories": [],
        "tags": [],
        "url": "http://localhost:4000/cheatsheets/virtualbox/",
        "teaser":null},{
        "title": "Regular Expression Tutorial",
        "excerpt":"1. Introduction Regular expressions are Python’s method to check some patterns in your program. # ignore errors import warnings warnings.filterwarnings(action='ignore') # 1. magic to print version # 2. magic so that the notebook will reload external python modules # https://gist.github.com/minrk/3301035 %load_ext watermark %load_ext autoreload %autoreload import pandas as pd import...","categories": ["python"],
        "tags": [],
        "url": "http://localhost:4000/RegularExpression/",
        "teaser":null},{
        "title": "Calculating the Balance in Your Retirement Account (GUI)",
        "excerpt":"Problem What age do you plan to retire? Whatever your age when you decide to retire, you have to consider how much you contribute to your retirement account, how much you would set your retirement spending. I created Wealth calculator at retirement, using GUI. If you are interested in creating...","categories": ["python"],
        "tags": [],
        "url": "http://localhost:4000/retirement/",
        "teaser":null},{
        "title": "Print the pattern (Math Set-1)",
        "excerpt":"Problem You a given a number N. You need to print the pattern for the given value of N. for N=2 the pattern will be 2 2 1 1 2 1 for N=3 the pattern will be 3 3 3 2 2 2 1 1 1 3 3 2 2...","categories": ["python"],
        "tags": [],
        "url": "http://localhost:4000/math1/",
        "teaser":null},{
        "title": "Print the table (Math Set-2)",
        "excerpt":"Problem Print the table of a given number N. Input: First line contains an integer, the number of test cases ‘T’. T testcases follow. Each testcase cotains one line of input denoting N. Output: For each testcase, print the table of N upto 10. Constraints: 1 &lt;= T &lt;= 100...","categories": ["python"],
        "tags": [],
        "url": "http://localhost:4000/math2/",
        "teaser":null},{
        "title": "A Song Of Ash And Smoke (MOT)",
        "excerpt":"Lyrics 재로 덮힌 하얀 마을에 재로 지은 하얀 집에 재가 되어버린 심장을 가진 하얀 재 소녀 타버린 피아노 앞에 앉아 타버린 마음 노래하죠 라 랄라 랄라 랄라 재로 덮힌 하얀 마을에 재로 지은 하얀 집에 숯이 되어버린 심장을 가진 까만 재 소년 타버린 기타를 들고 앉아 타버린 마음 노래하죠 라...","categories": [],
        "tags": ["music"],
        "url": "http://localhost:4000/A-Song-Of-Ash-And-Smoke-MOT/",
        "teaser":null},{
        "title": "SuperMario Orchestra",
        "excerpt":"  Concert Program   SuperMario World   [01] Opening Theme (0:00)   [02] Overworld (1:00)   [03] Level Clear (2:21)   [04] Boss (2:33)   [10] Ending Theme (12:00)   SuperMario 64   [05] Bob-Omb Battlefield (3:54)   [06] Slide (5:47)   [07] Dire, Dire Docks (6:43)   [08] Bowser’s Road (+Theme) (8:18)   [09] Staff Roll (10:14)  ","categories": [],
        "tags": ["music"],
        "url": "http://localhost:4000/SuperMario-Orchestra/",
        "teaser":null},{
        "title": "Madness (Muse)",
        "excerpt":"Lyrics I, I can’t get these memories out of my mind And some kind of madness has started to evolve, And I, I tried so hard to let you go But some kind of madness is swallowing me whole, yeah I have finally seen the light And I have finally...","categories": [],
        "tags": ["music"],
        "url": "http://localhost:4000/Madness-Muse/",
        "teaser":null},{
        "title": "Cloudy Seoul (MOT)",
        "excerpt":"Lyrics 서울은 흐림 시간은 느림 추억은 그림 그대는 흐림 서울은 흐림 생각은 느림 널 그린 그림 기억은 흐림 아무 말도 아무 일도 아무 예감도 없이 아무렇지 않게 하룬 가고 아무 말도 아무 일도 아무 예감도 없이 아무렇지 않게 나도 Translated Seoul, cloudy time, slow the memory, drawing you, blurry Seoul,...","categories": [],
        "tags": ["music"],
        "url": "http://localhost:4000/cloudy-Seoul-Mot/",
        "teaser":null},{
        "title": "Hope (Tentacion)",
        "excerpt":"Lyrics Rest in peace to all the kids that lost their lives in the Parkland shooting. This song is dedicated to you… Okay, she keep calling, she keep calling every single night Day and night, on my mind, please don’t kill the vibe Oh, no, I swear to God, I...","categories": [],
        "tags": ["music"],
        "url": "http://localhost:4000/Hope-Tentacion/",
        "teaser":null},{
        "title": "Pathfinding in Pacman domain",
        "excerpt":"Introduction Pathfinding builds on top of graph search algorithms and explore routes between nodes, traversing from the start node to the destination. These algorithms are used to identify optimal routes through a graph for uses such as logistics planning (Vehicle routing/logistics), least cost call or IP routing, and gaming simulation...","categories": ["AI"],
        "tags": [],
        "url": "http://localhost:4000/search-algorithms/",
        "teaser":null},{
        "title": "Demystifying Regularization",
        "excerpt":"Regularization Before discussing about regularization, we’ll do a quick recap on the notion of overfitting and the bias-variance tradeoff. Overfitting: So what is overfitting? Well, to put it in more simple terms it’s when we built a model that is too complex that it matches the training data “too closely”...","categories": ["machine-learning-project"],
        "tags": [],
        "url": "http://localhost:4000/regularization_L1L2/",
        "teaser":null},{
        "title": "Machine Learning.",
        "excerpt":"Introduction (Notes from a reading of Cohen and Welling: Steerable CNNs.) Consider \\(\\mathbb{R}^2\\) as an affine hyperplane in \\(\\mathbb{R}^3\\), embedded via the map \\(x\\mapsto (x,1)\\). Then the Euclidean motion group \\(\\tilde G = \\mathbb{R}^2\\ltimes O(2)\\) has a convenient matrix representation. Let \\(r\\) be a rotation and \\(t\\) a translation. Then...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/math-example/",
        "teaser":null},{
        "title": "Machine Learning Basic_1",
        "excerpt":"Introduction Why machine learning? Many industry companies use machine learning to be specialized and differentiated by intelligent applications. For instance, early days, Amazon disrupted the retail market by introducing product recommendations to their website, Google disrupted the advertising market by targeting the new customers who have similar behaviors to the...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/MLbasic1/",
        "teaser":null},{
        "title": "Regression1",
        "excerpt":"1. Linear Regression Consider a linear regression: \\(\\text{Given} \\; \\begin{cases} x_{i} \\; \\text{: inputs} \\\\ y_{i} \\; \\text{: outputs} \\end{cases}\\) , Find \\(\\theta_{0}\\) and \\(\\theta_{1}\\) \\[x= \\begin{bmatrix} x_{1} \\\\ x_{2} \\\\ \\vdots \\\\ x_{m} \\end{bmatrix}, \\qquad y= \\begin{bmatrix} y_{1} \\\\ y_{2} \\\\ \\vdots \\\\ y_{m} \\end{bmatrix} \\approx \\hat{y}_{i} = \\theta_{0}...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/regression1/",
        "teaser":null},{
        "title": "Regression2 (Overfitting and Regularization)",
        "excerpt":"1. Overfitting import warnings warnings.filterwarnings(action='ignore') # ignore errors # 1. magic for inline plot # 2. magic to print version # 3. magic so that the notebook will reload external python modules # 4. magic to enable retina (high resolution) plots # https://gist.github.com/minrk/3301035 %matplotlib inline %load_ext watermark %load_ext autoreload %autoreload...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/regression2/",
        "teaser":null},{
        "title": "Regression3 (Regression Applications)",
        "excerpt":"Regression Examples 1. De-noising Signal We start with a signal represented by a vector \\(x \\in \\mathbb{R}^n\\). The coefficients \\(x_i\\) correspond to the value of some function of time, evaluated (or sampled, in the language of signal processing) at evenly spaced points. It is usually assumed that the signal does...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/regression3/",
        "teaser":null},{
        "title": "Into. to APIs and Web",
        "excerpt":"API Introduction An API (Application programmable Interface) communicates between your personal device and data/service. In simple words, to help interactions between multiple softwares. It is an easy-to-use tool like GUI or UI. | Fig1. API Overview| Think of the case that you want to order a delivery food. You choose...","categories": ["web"],
        "tags": [],
        "url": "http://localhost:4000/api/",
        "teaser":null},{
        "title": "Data Crawling with Twitter API",
        "excerpt":"Introduction In the earlier post, I briefly introduced about how API and web work. In this post, let me talk about the practical usage of API: data crawling using Twitter API. Get Consumer Key (API key) and Access Key (Access token) If you want access to Twitter’s APIs, you should...","categories": ["web"],
        "tags": [],
        "url": "http://localhost:4000/Data-Crawling-TwitterAPI/",
        "teaser":null},{
        "title": "Data Crawling with Scrapy",
        "excerpt":"What is Scrapy Scrapy can be used for 1) extracting the data from websites and 2) saving them in your preferred format. In general, data crawling can be done easily if collecting data is small. However, as your data size gets bigger, number of URLs and that of crawler source...","categories": ["web"],
        "tags": [],
        "url": "http://localhost:4000/Data-Crawling-Scrapy/",
        "teaser":null},{
        "title": "Data Matching (Recordlinkage and Fuzzymatcher)",
        "excerpt":"1. Introduction Record Linkage aka data matching/merging is to join the information from a variety of data sources. The recordlinkage and fuzzymaker are used for process of joining two data sets when they don’t have a common unique identifier. This problem is a common business challenge and difficult to solve...","categories": ["EDA"],
        "tags": [],
        "url": "http://localhost:4000/data-matching/",
        "teaser":null},{
        "title": "Database System and SQL",
        "excerpt":"1. Introduction SQL is a simple yet powerful language that helps analysts/developers manage and query data directly from a database, without having to copy it first. 2. Data/Database Data is distinct pieces of information and A database is a well-organized collection of data that is stored in an electronic format....","categories": ["SQL"],
        "tags": [],
        "url": "http://localhost:4000/sql1/",
        "teaser":null},{
        "title": "Deep Learning Performance Improvement 1 - Parameter Initialization",
        "excerpt":"Parameter Initialization Importance of Parameter Initialization To build a machine learning algorithm, we use ideas from defined models such as Linear Regression, Logistic Regression, Support Vector Machine, CNN, RNN, etc. The follwoing is a common training process: Initialize parameters Choose Optimizer Repeat the steps: Forward-Propagation with inputs Compute Loss function...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/Parameter_Initialization/",
        "teaser":null},{
        "title": "Deep Learning Performance Improvement 2 - Optimizer",
        "excerpt":"Optimizer Importance of Optimization In Machine Learning, we can think of improvement mainly in four parts: initialization, optimization, regularzation, and gradient check). As a reminder, a common training process is shown below: Initialize parameters Choose Optimizer Repeat the steps: Forward-Propagation with inputs Compute Loss function after determining which one you...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/Optimization_methods/",
        "teaser":null},{
        "title": "Deep Learning Performance Improvement 3 - Regularization",
        "excerpt":"Regularization Regularization is used for a model to predict better. For Deep Learning models, overfitting commonly happens if the training dataset is not big enough so penalizing technique (L1 called LASSO and L2 called Ridge) and dropout technique will be introduced. Then such overfitting problem like predicting well on a...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/Regularization/",
        "teaser":null},{
        "title": "Deep Learning Performance Improvement 4 - Back-propagation",
        "excerpt":"Back-propagation Importance of Back-propagation Due to improvement of open source tools like Tensorflow or Keras, it seems easier to code up classification of cat or dog based on CNN without understanding. Unfortunately, these tools let us be tempted to avoid understanding of the algorithms. In particular, not understanding back-propagation would...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/Backpropagation/",
        "teaser":null},{
        "title": "Deep Learning Applications in Computer Vision",
        "excerpt":"Applications in Computer Vision Even though there are many challenging problems in computer vision, I would like to categorize them into 8 so far and introduce important papers for each type. 1. Image Classification Image classification is the task of classifying image into one of the pre-defined categories. The most...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/cv_intro/",
        "teaser":null},{
        "title": "Deep Learning Applications in Computer Vision",
        "excerpt":"Applications in Computer Vision Even though there are many challenging problems in computer vision, I would like to categorize them into 8 so far and introduce important papers for each type. 1. Image Classification Image classification is the task of classifying image into one of the pre-defined categories. The most...","categories": ["machine-learning-concept"],
        "tags": [],
        "url": "http://localhost:4000/",
        "teaser":null}]
