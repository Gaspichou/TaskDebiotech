echo "Checking Python version"

if ! python_version=$(python3 --version 2>&1); then
    echo "Python 3 is not installed"
    exit 1
else
    echo $python_version
    echo ""
fi

echo "Installing packages"
pip3 install schedule
pip3 install datetime
echo ""

echo "Running Python code"
python3 main.py