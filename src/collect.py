startTime = time.strftime('%Y-%m-%d_%H.%M.%S')

withDebugInfo = True
for arg in sys.argv:
    if arg == '--no-debug':
        withDebugInfo = False
if withDebugInfo:
    GLv_logFile = open(f'{startTime}_debug.log', 'w', newline='')

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main(credentials, maxWorkers, routes, routers))

routers.update_db()
routes.update_db(routers, startTime)

if GLv_logFile:
    db2csv('routes', startTime)
    db2csv('routers', startTime)
    db2csv('routes_trkr', startTime)
    GLv_logFile.close()