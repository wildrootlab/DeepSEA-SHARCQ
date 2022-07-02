import uvicorn
def main():
    uvicorn.run("main:app", port=5000, log_level="info")
main()